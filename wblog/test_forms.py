from django.test import TestCase
from .forms import NewPostForm, CommentForm


class TestNewPostForm(TestCase):

    def test_add_post_valid(self):
        form = NewPostForm(data={
            'title': 'post1',
            'content': 'post content'
        })
        self.assertTrue(form.is_valid())

    def test_add_post_valid_no_data(self):
        form = NewPostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)



class TestCommentForm(TestCase):

    def test_add_post_valid(self):
        form = CommentForm(data={
            'body': 'post1'
        })
        self.assertTrue(form.is_valid())

    def test_add_post_valid_no_data(self):
        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

