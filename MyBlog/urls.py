from django.conf.urls import patterns, include, url

from blog.views import main,page_view,cate_view,tag_view,archive_view,searchView
from blog.feeds import LatestEntriesFeed
# import tinymce
# import mce_filebrowser
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyBlog.views.home', name='home'),
    # url(r'^MyBlog/', include('MyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^category/(?P<cate_id>\d+)/$',cate_view),
    url(r'^articles/(?P<post_id>\d+)/$',page_view,name="articles"),
    # url(r'^articles/(?P<post_id>\d+)/add_comment/$',add_comment),
    url(r'^tags/(?P<tag_id>\d+)/$',tag_view),
    url(r'^date/(?P<year>\d+)/(?P<month>\d+)/$',archive_view),
    url(r'^searchResult/$',searchView),

    url(r'^$',main),
    url(r'^comments/', include('django.contrib.comments.urls')),

    (r'^tinymce/', include('tinymce.urls')),
    (r'^mce_filebrowser/', include('mce_filebrowser.urls')),

    url(r'^latest/feeds/$',LatestEntriesFeed()),
)
# for captcha  human validation
# urlpatterns += patterns('',
#     url(r'^captcha/', include('captcha.urls')),
# )
# for django-filebrowser  installation
# from filebrowser.sites import site
# urlpatterns+=patterns('',
#     url(r'^admin/filebrowser/',include(site.urls)),
#     url(r'grappelli/',include('grappelli.urls'))
# )

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^static/(?P<path> .*)$', 'django.views.static.serve',
                                   { 'document_root': settings.STATIC_ROOT, }), )
    urlpatterns+=staticfiles_urlpatterns()

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))


handler404='blog.views.my_custom_404_view'
