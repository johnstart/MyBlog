# Create your views here.
# -*- coding: cp936 -*-

# from django.template import loader,Context
# from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.core.paginator import Paginator,InvalidPage,EmptyPage
# from django.core.urlresolvers import reverse
from models import *
from django.db.models import Q
from django.template import RequestContext

from django.utils import timezone

import datetime


def getBlogsOfDate(year,month):
    blogs=Post.objects.filter(timestamp__year=year,timestamp__month=month)
    return blogs

def getArchive():
    temp=[]

    first=Post.objects.order_by('timestamp')[0]
    first_year=first.timestamp.year
    first_month=first.timestamp.month

    today=datetime.datetime.today()
    this_year=today.year
    this_month=today.month
    for year in range(first_year,this_year+1):
        for month in range(1,13):
            num=len(getBlogsOfDate(year,month))
            if num>0:
                archiveName=u"%d年 %d月(%d)"%(year,month,num)
                urlName="/date/%d/%d"%(year,month)
                temp.append((archiveName,urlName))
    return temp

from math import log
def tagcloud(threshold=0,maxsize=10,minsize=1):
    """usage:
        -threshold: Tag usage less than the threshold is excluded from
            being displayed.  A value of 0 displays all tags.
        -maxsize: max desired CSS font-size in some units  will be turned into em
        -minsize: min desired CSS font-size in some units
    Returns a list of dictionaries of the tag, its count and
    calculated font-size.
    """
    counts,taglist,tagcloud=[],[],[]
    tags=Tag.objects.all()
    for tag in tags:
        count=tag.post_set.count()
        # if count>= threshold:
        counts.append(count), taglist.append(tag)
    maxcount = max(counts)
    mincount = min(counts)
    constant = log(maxcount - (mincount - 1))/(maxsize - minsize or 1)
    tagcount = zip(taglist, counts)
    for tag, count in tagcount:
        size = log(count - (mincount - 1))/(constant or 1) + minsize
        size=int(size)
        tagcloud.append({'tag': tag, 'count': count, 'size': size})
    return tagcloud

#处理器允许你设置一些变量，它们会在每个context中自动被设置好，而不必每次调用 render_to_response()
#  时都指定。要点就是，当你渲染模板时，你要用 RequestContext 而不是 Context 。
def getCommon(request):
    archives=getArchive()
    # see : https://docs.djangoproject.com/en/1.4/topics/i18n/timezones/
    #now=datetime.datetime.utcnow().replace(tzinfo=utc)
    now=timezone.now()
    latest_posts=Post.objects.filter(timestamp__gte=(now-datetime.timedelta(days=30)))
    # latest_comments=Comment.objects.filter(createTime__gte=(now-datetime.timedelta(days=30)))
    Cate=BlogCategory.objects.all()
    tagc=tagcloud()

    return locals()

def main(request):
    """Main listing"""
    posts=Post.objects.all().order_by('-timestamp')
    paginator=Paginator(posts,5)
    try:
        page=int(request.GET.get("page","1"))
    except ValueError:
        page=1
    try:
        posts=paginator.page(page)
    except (InvalidPage,EmptyPage):
        posts=paginator.page(paginator.num_pages)

    return render_to_response("mainPage.html",dict(posts=posts),
                              context_instance=RequestContext(request,processors=[getCommon]))


def page_view(request,post_id):
    post=Post.objects.get(pk=post_id)
    # comments=post.comment_set.all()
    # if request.method == 'POST':
    #     c=request.POST  #no problem
    #     form=addComment(c)
    #     if form.is_valid():
    #         cd=form.cleaned_data
    #         now=datetime.datetime.now()
    #         new_comment=Comment(author=cd['name'],email=cd['e_mail'],
    #                             body=cd['content'],createTime=now,post=Post.objects.get(pk=post_id))
    #         new_comment.save()
    # else:
    post.readTimes+=1
    post.save()
    #You should use RequestContext instead of Context
    return render_to_response("pageView.html",locals(),
                              context_instance=RequestContext(request,processors=[getCommon]))

# def add_comment(request,post_id):
#     now=datetime.datetime.now()
#     name=request.GET['name']
#     email=request.GET['email']
#     content=request.GET['commentContent']
#
#     new_comment=Comment(author=name,email=email,body=content,createTime=now,post=Post.objects.get(pk=post_id))
#     new_comment.save()
#
#     return HttpResponseRedirect('/articles/'+str(post_id))

# category
def cate_view(request,cate_id):
    category=BlogCategory.objects.get(pk=cate_id)
    return render_to_response("category.html",dict(category=category),
                              context_instance=RequestContext(request,processors=[getCommon]))
#for each tag
def tag_view(request,tag_id):
    tag=Tag.objects.get(pk=tag_id)
    posts=Post.objects.filter(tags__id=tag_id)
    return render_to_response("tagView.html",locals(),
                              context_instance=RequestContext(request,processors=[getCommon]))

def archive_view(request,year,month):
    archiveName=u"%s 年%s 月"%(year,month)
    posts=getBlogsOfDate(int(year),int(month))
    return render_to_response("archiveView.html",locals(),
                              context_instance=RequestContext(request,processors=[getCommon]))

def searchView(request):
    query=request.GET.get('s','')
    if query:
        qset=(
            Q(title__icontains=query)|
            Q(body__icontains=query)
        )
        results=Post.objects.filter(qset).distinct()
    else:
        results=[]

    return render_to_response('searchView.html',locals(),
                              context_instance=RequestContext(request,processors=[getCommon]))

def my_custom_404_view(request):
    return render(request,'404_test.html',{},status=404)


# from forms import PictureForm
# def addPicture(request):
#     if request.method == 'POST':
#         form = PictureForm(request.POST, request.FILES)
#         if form.is_valid():
#             f = request.FILES["imagefile"]
#             # des_origin_path 为你在服务器上保存原始图片的文件物理路径
#             des_origin_f = open("E:\MyPic", "ab")
#             for chunk in f.chunks():
#                 des_origin_f.write(chunk)
#             des_origin_f.close()
#             return HttpResponseRedirect('/addComment/thanks/')
#     else:
#         form=PictureForm()
#
#     return render_to_response('UpLoadPic.html',locals(),context_instance=RequestContext(request))






