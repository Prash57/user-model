from django.shortcuts import render, redirect
from .models import Feed, Tag
from .forms import *

# Create your views here.


def com_home(request):
    feeds = Feed.objects.all()
    context = {'feeds': feeds}
    return render(request, 'community/c_home.html', context)


def addFeed(request):
    profile = request.user.profile
    form = FeedForm()
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()

        form = FeedForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = profile
            post.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                post.tags.add(tag)

            return redirect('c_home')

    context = {'form': form}
    return render(request, 'community/feed_form.html', context)


def editFeed(request, pk):
    profile = request.user.profile
    feed = profile.feed_set.get(id=pk)
    form = FeedForm(instance=feed)
    if request.method == 'POST':
        form = FeedForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return redirect('c_home')

    context = {'form': form}
    return render(request, 'community/edit_feed.html',context)

def deleteFeed(request, pk):
    feed = Feed.objects.get(id=pk)
    if request.method == 'POST':
        feed.delete()
        return redirect('c_home')
        
    context = {'objects': feed}
    return render(request, 'community/delete_feed.html', context)

