from django.shortcuts import render
from django.http import Http404

# Fake blog data for now (later you can connect a database model)
BLOG_POSTS = [
    {"id": 1, "title": "First Blog Post", "content": "This is my first post!"},
    {"id": 2, "title": "Second Blog Post", "content": "Another update on my journey."},
]

def blog_list(request):
    return render(request, 'blog_list.html', {'posts': BLOG_POSTS})

def blog_detail(request, post_id):
    # Find post by ID
    post = next((post for post in BLOG_POSTS if post["id"] == post_id), None)
    if not post:
        raise Http404("Post not found")
    return render(request, 'blog_detail.html', {'post': post})

