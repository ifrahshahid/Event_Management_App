from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from my_event_manager.events.models import Event

User = get_user_model()

class EventTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@example.com', password='password123')
        self.client.force_authenticate(user=self.user)
        self.url = '/api/events/'  

    def test_create_event(self):
        data = {
            'title': 'Test Event',
            'description': 'Event description',
            'date': '2024-09-30T00:00:00Z',
            'location': 'Test Location'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().title, 'Test Event')

    def test_list_events(self):
        Event.objects.create(
            title='Test Event 1',
            description='Description 1',
            date='2024-09-30T00:00:00Z',
            location='Location 1',
            owner=self.user
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_event(self):
        event = Event.objects.create(
            title='Test Event 1',
            description='Description 1',
            date='2024-09-30T00:00:00Z',
            location='Location 1',
            owner=self.user
        )
        url = f'/api/events/{event.id}/'  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Event 1')


    def test_update_event(self):
        event = Event.objects.create(
            title='Old Title',
            description='Old Description',
            date='2024-09-30T00:00:00Z',
            location='Old Location',
            owner=self.user
        )
        url = f'/api/events/{event.id}/'
        data = {'title': 'New Title'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        event.refresh_from_db()
        self.assertEqual(event.title, 'New Title')


    def test_delete_event(self):
        event = Event.objects.create(
            title='Event to Delete',
            description='Description',
            date='2024-09-30T00:00:00Z',
            location='Location',
            owner=self.user
        )
        url = f'/api/events/{event.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Event.objects.count(), 0)



    def test_attend_event(self):
        event = Event.objects.create(
            title='Event to Attend',
            description='Description',
            date='2024-09-30T00:00:00Z',
            location='Location',
            owner=self.user
        )
        url = f'/api/events/{event.id}/attend/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user, event.attendees.all())


    def test_attend_event_already_attending(self):
        event = Event.objects.create(
            title='Event to Attend Again',
            description='Description',
            date='2024-09-30T00:00:00Z',
            location='Location',
            owner=self.user
        )
        event.attendees.add(self.user)
        url = f'/api/events/{event.id}/attend/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'You are already attending this event.')












