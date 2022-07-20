from email.mime import image
from django.shortcuts import render, redirect
from .models import DevTool, Post
from .form import PostForm, ToolForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, template_name='ideas/home.html', context=context)

def create(request):
    tools = DevTool.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(f"/post/{post.id}")
    
    context = {
        "tools": tools,
    }
    return render(request, template_name="ideas/create.html", context=context)

def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post": post,
    }
    return render(request, template_name="ideas/detail.html", context=context)

def update(request, id):
    post = Post.objects.get(id=id)
    tools = DevTool.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            if form.cleaned_data['image']:
                post.image = form.cleaned_data['image']
            post.content = form.cleaned_data['content']
            post.interest = form.cleaned_data['interest']
            post.devtool = form.cleaned_data['devtool']
            post.save()
        return redirect(f"/post/{id}")
    
    form = PostForm(instance=post)
    context = {
        "tools": tools,
        "post": post,
        "form": form,
        "id": post.id,
    }
    return render(request, template_name="ideas/update.html", context=context)

def delete(request, id):
    if request.method == "POST":
        Post.objects.filter(id=id).delete()
        return redirect("/")

def tool_list(request):
    tools = DevTool.objects.all()
    context = {
        'tools': tools,
    }
    return render(request, template_name='tools/list.html', context=context)

def tool_create(request):
    if request.method == "POST":
        form = ToolForm(request.POST)
        if form.is_valid():
            tool = form.save()
            return redirect(f"/tool/post/{tool.id}")
    
    context = {
        
    }
    return render(request, template_name="tools/create.html", context=context)

def tool_detail(request, id):
    tool = DevTool.objects.get(id=id)
    all_post = tool.post_set.all()
    context = {
        "tool": tool,
        "all_post": all_post,
    }
    return render(request, template_name="tools/detail.html", context=context)

def tool_update(request, id):
    tool = DevTool.objects.get(id=id)
    if request.method == "POST":
        form = ToolForm(request.POST)
        if form.is_valid():
            tool.name = form.cleaned_data['name']
            tool.kind = form.cleaned_data['kind']
            tool.content = form.cleaned_data['content']
            tool.save()
        return redirect(f"/tool/post/{id}")
    
    form = ToolForm(instance=tool)
    context = {
        "form": form,
        "id": tool.id,
    }
    return render(request, template_name="tools/update.html", context=context)

def tool_delete(request, id):
    if request.method == "POST":
        DevTool.objects.filter(id=id).delete()
        return redirect("/tool/list")