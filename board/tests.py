from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group, AnonymousUser
from .models import Post, Category
from accounts.models import MyUser

# Create your tests here.

class TestPost(TestCase):

    def setUp(self):
        self.client = Client()
        # create groups
        group_admin = Group.objects.create(name='Admin')
        group_editor = Group.objects.create(name='Editor')
        group_custom = Group.objects.create(name='Custom_user')

        # create user
        self.anonymous = AnonymousUser()
        self.admin = User.objects.create_user(username='admin',
                                         first_name='first_admin',
                                         last_name='second_admin',
                                         email='admin@mail.com',
                                         password='test_admin_pass')
        self.admin.groups.add(group_admin)
        self.editor = User.objects.create_user(username='editor',
                                               first_name='first_editor',
                                               last_name='last_editor',
                                               email='editor@mail.com',
                                               password='test_editor_pass')
        self.editor.groups.add(group_editor)
        self.custom = User.objects.create_user(username='custom',
                                               first_name='first_custom',
                                               last_name='last_custom',
                                               email='custom@mail.com',
                                               password='test_custom')
        self.custom.groups.add(group_custom)

        self.my_admin = MyUser.objects.create(user=self.admin, birth_day='1990-05-02')
        self.my_custom = MyUser.objects.create(user=self.custom, birth_day='1991-06-01')
        self.my_editor = MyUser.objects.create(user=self.editor, birth_day='1992-07-05')

        self.category = Category.objects.create(category='test-category')

    def test_access_url(self):
        url = reverse('post-create')
        self.client.login(username=self.admin,
                          password='test_admin_pass')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_forbidden_access(self):
        url = reverse('post-create')
        self.client.login(username=self.anonymous)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_is_approve_admin(self):
        url = reverse('post-create')
        self.client.login(username=self.admin,
                          password='test_admin_pass')
        response = self.client.post(url, {'title': 'test title', 'content': 'test content',
                                          'category': 1})
        post = Post.objects.get(title='test title')
        self.assertEquals(post.is_approve, True)

    def test_is_approve_custom(self):
        url = reverse('post-create')
        self.client.login(username=self.custom,
                          password='test_custom')
        response = self.client.post(url, {'title': 'custom', 'content': 'test content',
                                          'category': 1})
        post = Post.objects.get(title='custom')
        self.assertEquals(post.is_approve, False)

    def test_is_approve_editor(self):
        url = reverse('post-create')
        self.client.login(username=self.editor,
                          password='test_editor_pass')
        response = self.client.post(url, {'title': 'editor', 'content': 'test content',
                                          'category': 1})
        post = Post.objects.get(title='editor')
        self.assertEquals(post.is_approve, True)
