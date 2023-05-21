from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Event, Attendee
from .forms import EventForm


def latest(request):
    """ A view to show all posts """

    events = Event.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'events/latest.html', context)


def event_listing(request, event_id):
    """ A view to show an event's information """

    product = get_object_or_404(Event, pk=product_id)

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

    template = 'latest/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def event_listing(request, event_id):
    """ A view to show full event details """

    event = get_object_or_404(Event, pk=product_id)

    context = {
        'event': event,
    }

    return render(request, 'latest/event_listing.html', context)


@login_required
def edit_event(request, event_id):
    """ Edit a product """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have authorisation to access this page.')
        return redirect(reverse('home'))

    event = get_object_or_404(Product, pk=event_id)
    if request.method == 'POST':
        event = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event listing was updated.')
            return redirect(reverse('event_listing', args=[event.id]))
        else:
            messages.error(request, 'Failed to update. Please check all details are correct and retry')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.title}')

    template = 'latest/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }
    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """Delete product """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have authorisation to access this page.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event deleted.')
    return redirect(reverse('latest'))


def register(request, event=event_id):
    """ Register attendance for event """

    if request.method == 'POST':
        form = AttendeeForm(request.POST, request.FILES)
        if form.is_valid():
            attendee = form.save()
            messages.success(request, 'Thank you, we have registered you successfully.')
            return redirect(reverse('latest'))
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = AttendeeForm()

    template = 'latest/event_listing.html'
    context = {
        'form': form,
    }

    return render(request, template, context)