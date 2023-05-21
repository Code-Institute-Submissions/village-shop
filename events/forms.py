from django import forms
from .models import Event, Attendee


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        self.fields['title'].widget.attrs['autofocus'] = True

class AttendeeForm(forms.ModelForm):

    class Meta:
        model = Attendee
        fields = '__all__'
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        self.fields['name'].widget.attrs['autofocus'] = True