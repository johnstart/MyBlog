__author__ = 'QJL'

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from models import Post

class LatestEntriesFeed(Feed):
    title="latest blogs"
    link="/siteblogs/"
    description="Update on changes and additions to blog posts"

    def items(self):
        return Post.objects.order_by('-timestamp')[:5]

    # def item_title(self,item):
    #     return item.title
    #
    # def item_description(self, item):
    #     return item.body

    def item_link(self, item):
        return reverse('articles',kwargs={'post_id':item.pk})

