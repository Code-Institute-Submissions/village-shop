from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Event, Post
from .forms import EventForm, PostForm


def events(request):
    """ A view to show all posts """

    events = Event.objects.all()
    # blogs will be listed from newest to oldest
    posts = Post.objects.all().order_by('-date_added')

    context = {
        'events': events,
        'posts': posts,
    }

    return render(request, 'events/latest.html', context)


def event_listing(request, event_id):
    """ A view to show an event's information """

    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'latest/event_listing.html', context)


@login_required
def add_event(request):
    """ Super user can create new event listings """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have authorisation to access this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Successfully created a new event listing')
            return redirect(reverse('event_listing', args=[event.id]))
        else:
            messages.error(request, 'Failed to add event. Please check the entry details are correct.')
    else:
        form = EventForm()

    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def event_listing(request, event_id):
    """ A view to show full event details """

    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'events/event_listing.html', context)


@login_required
def edit_event(request, event_id):
    """ Edit a product """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have authorisation to access this page.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event listing was updated.')
            return redirect(reverse('event_listing', args=[event.id]))
        else:
            messages.error(request, 'Failed to update. Please check all details are correct and retry')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing: {event.title}')

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }
    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """Delete event """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have authorisation to access this page.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event deleted.')
    return redirect(reverse('events'))


@login_required
def add_blog(request):
    """ Add a blog post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have authorisation to access this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'The blog post has been published.')
            return redirect(reverse('events'))
        else:
            messages.error(request, 'Failed to add the blog post. Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'events/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, post_id):
    """ Edit a Blog Post """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have authorisation to access this page.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post.')
            return redirect(reverse('edit_blog', args=[post.id]))
        else:
            messages.error(request, 'Failed to update blog post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing: {post.title}')

    template = 'events/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, post_id):
    """ Delete a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have authorisation to access this page.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Post, pk=post_id)
    blog.delete()
    messages.success(request, 'Blog post deleted.')
    return redirect(reverse('events'))
