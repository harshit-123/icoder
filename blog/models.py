from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    diff_category = [
        ('World', u'World'),
        ('US', u'US'),
        ('Technology', u'Technology'),
        ('Design', u'Design'),
        ('Culture', u'Culture'),
        ('Business', u'Business'),
        ('Science', u'Science'),
        ('Health', u'Health'),
        ('Travel', u'Travel'),
    ]
    sno         = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=255)
    content     = models.TextField()
    views       = models.IntegerField(default=0)
    author      = models.CharField(max_length=255)
    blog_image  = models.ImageField(upload_to="blog/img", default="")
    category    = models.CharField(max_length=255, choices=diff_category, null=True, blank=True)
    slug        = models.SlugField(max_length=200)
    timestamp   = models.DateTimeField(blank=True)

    class Meta:
        db_table = "Post"

    def __str__(self):
        return self.title+' By '+self.author
    

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    class Meta:
        db_table = "blog_comment"

    def __str__(self):
        if self.user.first_name != "":
            return self.comment[0:30]+"... " + "by " + self.user.first_name
        else:
            return self.comment[0:30]+"... " + "by " + self.user.username