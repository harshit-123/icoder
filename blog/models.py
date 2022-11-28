from django.db import models
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
    author      = models.CharField(max_length=255)
    blog_image  = models.ImageField(upload_to="blog/img", default="")
    category    = models.CharField(max_length=255, choices=diff_category, null=True, blank=True)
    slug        = models.SlugField(max_length=200)
    timestamp   = models.DateTimeField(blank=True)

    class Meta:
        db_table = "Post"

    def __str__(self):
        return self.title+' By '+self.author
    