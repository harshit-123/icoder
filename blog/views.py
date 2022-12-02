from django.shortcuts import render, redirect
from django.contrib import messages
from blog.models import Post, BlogComment
from blog.templatetags import extras
# Create your views here.
def bloghome(request):
    allPosts = Post.objects.all()
    context = {
        'allPosts': allPosts
    }
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug= slug)[0]
    comments = BlogComment.objects.filter(post= post, parent=None)
    replies = BlogComment.objects.filter(post= post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    print("replyDict===>",replyDict)
    params = {
        "post": post,
        "comments": comments,
        "user": request.user,
        "replyDict": replyDict
    }
    return render(request, 'blog/blogPost.html', params)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        print("comment===>", comment)
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        print("parent_sno==>",parentSno)
        if parentSno =="":
            print("parent sno in if==>",parentSno)
            comment = BlogComment(comment = comment, user = user, post = post)
            comment.save()
            messages.success(request, "Your comment has been Posted Successfully!")
        else:
            print("parent sno in else==>", parentSno)
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment = comment, user = user, post = post, parent = parent)
            comment.save()
            messages.success(request, "Your Reply has been posted successfully!")
    return redirect(f"/blog/{post.slug}")

