from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Events
from .views import index, getResources, getMeeting
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import ResourceForm

class MeetingTest(TestCase):
    def test_string(self):
        mt = Meeting(meetingtitle = "Member Initiation")
        self.assertEqual(str(mt), mt.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
    def test_string(self):
        reso = Resource(resourcename = "BiPolar - It's not just being sad")
        self.assertEqual(str(reso), reso.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_string(self):
        event = Events(eventname = "Snek Dance")
        self.assertEqual(str(event), event.eventname)

    def test_table(self):
        self.assertEqual(str(Events._meta.db_table), 'events')

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class getResourcesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)

# ---------- FORMS ----------
class ResourceFormTest(TestCase):
    def test_typeform_is_valid(self):
        form=ResourceForm(
            data={
                'resourcename' : "newresource", 
                'resourcetype' : "movie", 
                'resourceURL' : "madlove.com", 
                'user' : "billiebipolar", 
                'rating' : "5stars",
                'reviewtext' : "it's a great thing to have a movie about being bipolar and in love",

            }
        )
        self.assertTrue(form.is_valid())
        
