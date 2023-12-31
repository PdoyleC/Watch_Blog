import uuid
from cloudinary.uploader import upload
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from django.utils.text import slugify
from .forms import CommentForm, NewPostForm, ContactForm


class PostList(generic.ListView):
    """
    Post List view to show all watches
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(LoginRequiredMixin, View):
    """
    This part of the code is copied from code institude walkthrough
    'I think therefore I blog'. This section views the post
    detail according to the title.
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    """
    Likes an Post
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class NewPost(View):
    """
    Creates a new Post
    """
    def get(self, request):
        form = NewPostForm()
        return render(request, 'new_post.html', {'form': form})

    def post(self, request):
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            unique_id = uuid.uuid4().hex[:5]
            post.slug = "{}-{}".format(slugify(post.title), unique_id)
            post.status = 1
            post.save()
            messages.success(request, 'Post added successfully!')

            return HttpResponseRedirect(reverse(
                'post_detail', args=[post.slug]))
        return render(request, 'new_post.html', {'form': form})


class EditPost(View):
    """
    Edits an Post
    """
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if not request.user.is_authenticated:
            return redirect('post_detail', slug=slug)
        else:
            form = NewPostForm(instance=post)
            return render(request, 'edit_page.html', {
                'form': form, 'post': post, 'editing': True})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if request.user == post.author:
            form = NewPostForm(request.POST, instance=post)
            if form.is_valid():
                edited_post = form.save(commit=False)
                unique_id = uuid.uuid4().hex[:5]
                edited_post.slug = "{}-{}".format(
                    slugify(post.title), unique_id)

                # Enables editing of image
                if 'featured_image' in request.FILES:
                    edited_image = request.FILES['featured_image']
                    uploaded_image = upload(edited_image)
                    edited_post.featured_image = uploaded_image['url']

                edited_post.save()
                messages.success(request, 'Your post has successfully been' +
                                 ' edited!')
                return redirect('post_detail', slug=edited_post.slug)
            else:
                return render(request, 'edit_page.html', {
                    'form': form, 'post': post, 'editing': True})
        else:
            return redirect('post_detail', slug=slug)


def contact(request):
    """
    For the contact page
    """
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return HttpResponseRedirect('/contact?submitted=True')
            return redirect('home')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


class DeletePost(View):
    """
    Deletes an Post
    """
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'post_delete.html', {'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        if request.user == post.author:
            post.delete()
            messages.success(
                request, 'Your post has successfully been deleted!')
            return redirect('home')
        else:
            return redirect('post_detail', slug=slug)
