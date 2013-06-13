from django.db import models
from django.contrib import admin
# Create your models here.

#----blog category such as algorithm,programming,computer vison, machine learning----
class BlogCategory(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    title=models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s'%self.title

#--blog -------
from ckeditor.fields import RichTextField
class Post(models.Model):
    title=models.CharField(max_length=150)
    body=RichTextField()
    timestamp=models.DateTimeField()
    readTimes=models.PositiveIntegerField(editable=False,default=0)
    category=models.ForeignKey(BlogCategory)
    tags=models.ManyToManyField(Tag)

    class Meta:
        ordering=["-timestamp"]

    def __unicode__(self):
        return self.title

#----comments about each blog----
# class Comment(models.Model):
#     author=models.CharField(max_length=60)
#     email=models.EmailField()
#     body=models.TextField()
#     post=models.ForeignKey(Post)
#     createTime=models.DateTimeField(auto_now_add=True)
#
#     def __unicode__(self):
#         return u"%s:%s"%(self.post,self.body[:50])

from mce_filebrowser.admin import MCEFilebrowserAdmin
class PostAdmin(MCEFilebrowserAdmin):
    list_display = ('title','timestamp')
    filter_horizontal = ['tags',]  #for a beautiful view to choose tags

# class CommentAdmin(admin.ModelAdmin):
#     display_fields=["post","author"]

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','detail')

class TagAdmin(admin.ModelAdmin):
    display_fields=["title",]

admin.site.register(Post,PostAdmin)
# admin.site.register(Comment,CommentAdmin)
admin.site.register(BlogCategory,BlogCategoryAdmin)
admin.site.register(Tag,TagAdmin)

#---test models for ckeditor

class News(models.Model):
    content=RichTextField()

class NewsAdmin(admin.ModelAdmin):
    display_fields=["content",]

admin.site.register(News,NewsAdmin)