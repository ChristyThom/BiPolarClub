from django import forms
from .models import Meeting, MeetingMinutes, Resource, Events

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'