from django.test import TestCase, Client
from authentication.models import CustomUser
from .models import Voting, Vote


class AddVotingTestCase(TestCase):

    def setUp(self):
        user = CustomUser.objects.create_user(email="test@mail.com",
                                               password="123!qwerty")
        self.client = Client()
        user_login = self.client.login(username="test@mail.com",
                                        password="123!qwerty")
    
    def test_add_voting(self):
        header = "Header"
        description = "Description"
        data = self.client.post('/create_voting', data = {"header": header,
                 "description": description})
        code = data.status_code
        self.assertEqual(code, 302)
        db_data = Voting.objects.get(header=header).description
        self.assertEqual(description, db_data)
    
    def test_empty_fields(self):
        data = self.client.post('/create_voting')
        self.assertIn(b"Empty Header or Description", data.content)
    
    def test_empty_header(self):
        data = self.client.post('/create_voting', data = {"description": "Test Header"})
        self.assertIn(b"Empty Header or Description", data.content)

    def test_empty_description(self):
        data = self.client.post('/create_voting', data = {"header": "Test Description"})
        self.assertIn(b"Empty Header or Description", data.content)


class VotingPageTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(email="test@mail.com",
                                               password="123!qwerty")
        self.client = Client()
        user_login = self.client.login(username="test@mail.com",
                                        password="123!qwerty")
        
        self.voting = Voting.objects.create(header='header', description='description', user_id=self.user)

    def test_true_vote(self):
        response = self.client.post(f'/votings/{self.voting.id}', data = {"vote": "yes"})
        self.assertEqual(response.status_code, 200)
        db_data = Vote.objects.get(voter_id=self.user, voting_id=self.voting)
        self.assertIsNotNone(db_data)
    
    def test_twice_voting(self):
        response = self.client.post(f'/votings/{self.voting.id}', data = {"vote": "yes"})
        second_response = self.client.post(f'/votings/{self.voting.id}', data = {"vote": "yes"})
        print(response)
        print(second_response)