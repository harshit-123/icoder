from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

#templates
def home(request):
    allPosts = Post.objects.all()
    context = {
        'allPosts': allPosts
    }
    return render(request, 'home/home.html',context)

def contact(request):
    if request.method == 'POST':
        name    = request.POST.get("name")
        email   = request.POST.get("email")
        phone   = request.POST.get("phone")
        content = request.POST.get("content")
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please Fill form correctly")  
        else:    
            contact = Contact(name = name, email = email, phone = phone, content = content)
            contact.save()
            messages.success(request, "Your Message has been Successfully Sent!")
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allBlogPosts = Post.objects.none() # this will create empty query set
    else:
        allBlogPostsTitle   = Post.objects.filter(title__icontains=query)
        allBlogPostsContent = Post.objects.filter(content__icontains=query)
        allBlogPosts        = allBlogPostsTitle.union(allBlogPostsContent)
    if allBlogPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your Query")  
    params = {
        "allBlogPosts": allBlogPosts,
        "query": query
    }
    return render(request, 'home/search.html', params)

def about(request):
    return render(request, 'home/about.html')

# Authentication APIs
def handleSignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #validations
        if len(username) > 10:
            messages.error(request, "Username must under 10 characters")
            return redirect("/")

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect("/")

        if pass1 != pass2:
            messages.error(request, "Password and confirm password do not match")
            return redirect("/")
        # create User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been Successfully Created!")
        return redirect("/")
    else:
        return HttpResponse("404- Not Found")

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['loginusername']
        password = request.POST['loginpass']

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged in")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials!, Please try again")
            return redirect("/")
    else:
        return HttpResponse("404- Not Found")

def handleLogout(request):
    logout(request)
    messages.warning(request, "Successfully Logged out!")
    return redirect("/")