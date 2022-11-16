from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm, MessageForm, IdentificationForm, GroupForm
from .models import Profile, Group
from community.views import com_home
from social.views import soc_home

# Create your views here.


def home(request):
    return render(request, 'index.html')


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid username')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'base/login.html')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User Registered')

            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, 'User not Registered')

    context = {'form': form}
    return render(request, 'base/register.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('index')


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'base/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'base/profile.html', context)


def account(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'base/account.html', context)


def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')
    context = {'form': form}
    return render(request, 'base/edit_account.html', context)


def deleteProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Account deleted successfully')
        return redirect('login')

    context = {'object': profile}
    return render(request, 'base/delete_account.html', context)


def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()

    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request, 'base/inbox.html', context)


def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read == True
        message.save()

    context = {'message': message}
    return render(request, 'base/message.html', context)


def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

        message.save()

        messages.success(request, 'Message sent successfully')
        return redirect('inbox')

    context = {'recipient': recipient, 'form': form}
    return render(request, 'base/message_form.html', context)


def verifyUser(request):
    profile = request.user.profile
    form = IdentificationForm()

    if request.method == 'POST':
        form = IdentificationForm(request.POST, request.FILES)
        if form.is_valid():
            verify = form.save(commit=False)
            verify.user = profile
            verify.save()
            messages.success(request, 'Verified')

        return redirect('account')

    context = {'form': form, 'profile': profile}
    return render(request, 'base/verify_form.html', context)


def groups(request):
    group = Group.objects.all()
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            if 'community':
                return com_home(request)
            elif 'social':
                return soc_home(request)
            else:
                return redirect('...')

    context = {'group': group, 'form': form}
    return render(request, 'base/groups.html', context)
