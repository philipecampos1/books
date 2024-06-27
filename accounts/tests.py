from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='philipe1',
            email='testeemail@hotmail.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'philipe1')
        self.assertEqual(user.email, 'testeemail@hotmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        def test_create_superuser(self):
            User = get_user_model()
            user = User.objects.create_user(
                username='philipesuper',
                email='testeemailsuper@hotmail.com',
                password='testpass123'
            )
            self.assertEqual(user.username, 'philipesuper')
            self.assertEqual(user.email, 'testeemailsuper@hotmail.com')
            self.assertTrue(user.is_active)
            self.assertTrue(user.is_staff)
            self.assertTrue(user.is_superuser)


# class SignupPageTests(TestCase):
#     def setUp(self):
#         url = reverse('signup')
#         self.response = self.client.get(url)

#     def test_signup_template(self):
#         self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(self.response, 'registration/signup.html')
#         self.assertContains(self.response, 'Sign Up')
#         self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

#     def test_signup_form(self):
#         form = self.response.context.get('form')
#         self.assertIsInstance(form, CustomUserCreationForm)
#         self.assertContains(self.response, 'csrfmiddlewaretoken')

#     def test_signup_view(self):
#         view = resolve('/accounts/signup/')
#         self.assertEqual(
#             view.func.__name__,
#             SignupPageView.as_view().__name__,
#         )


class SingupTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_singup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
