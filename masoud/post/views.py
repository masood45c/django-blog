from django.shortcuts import render, HttpResponse, get_object_or_404,HttpResponseRedirect, redirect
from django.contrib import messages
from .models import Post
from .forms import PostFrom

# Create your views here.
def index_view(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {"posts" : posts})

def create_view(request):
    form = PostFrom(request.POST or None)    
    if form.is_valid():
        post = form.save()
        messages.success(request, "Post created successfuly")
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
           "form" : form
        }
    return render(request,'post/form.html',context)




def detail_view(request, id):
    post = get_object_or_404(Post,id=id)
    return render(request,'post/detail.html',{"post":post})


def update_view(request,id):
    post = get_object_or_404(Post,id=id)
    form = PostFrom(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Post updated successfuly")

        return HttpResponseRedirect(post.get_absolute_url())

    context = {
           "form" : form
        }
    return render(request,"post/form.html", context)


def delete_view(request, id):
    post = get_object_or_404(Post,id=id)
    post.delete()

    return HttpResponseRedirect("/post/index")
    
