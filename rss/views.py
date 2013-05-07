from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from rss.models import Jobs

# We basically will provide an url like:
# /feeds/rss/<tag-name>/  => /feeds/rss/(?P<tag_name>[\w]+)/
# /feeds/atom/<tag-name>/ => /feeds/atom/(?P<tag_name>[\w]+)/
# And the generated RSS feed will list all the sorted 'Entry' which
# has been 'Tag'ed with <tag-name>.

class LatestFeed(Feed):
    """This is the class generating the simple RSS feed.
    """
    title = "MySiteName"
    link = "/"
    description = "My root description."
           
    def get_object(self, request, tag_name):
        """The 'tag_name' is passed from the urls.py
        """
        return get_object_or_404(Jobs, title=tag_name)

    
    def title(self, obj):
        """The root title tag content.
        """
        return "MySiteName: %s" % (obj.title)

    
    def items(self, obj):
        """The 'item' elements.
        """
        return Jobs.objects.filter(key_skills__icontains=obj).order_by('date_created')[:10]

        
    def item_title(self, item):
        return item.salary

    
    def item_link(self, item):
        return item.get_absolute_url()

    
    def item_description(self, item):
        return item.jobdetails
'''

class AtomEntryCustomFeed(Atom1Feed):
    """Custom Atom feed generator.
    This class will form the structure of the custom RSS feed.
    It's used to add a new tag element to each of the 'item's.
    """
    def add_item_elements(self, handler, item):
	# Invoke this same method of the super-class to add the standard elements
	# to the 'item's.
        super(AtomEntryCustomFeed, self).add_item_elements(handler, item)

	# Add a new custom element named 'content' to each of the tag 'item'.
        handler.addQuickElement(u"content", item['content'])


class AtomEntryFeed(RssEntryFeed):
    """Class used to generate the final customized Atom feed.
    Since this is a subclass of the RSS feed class it'll inherit its methods.
    """
    feed_type = AtomEntryCustomFeed		# Custom Atom feed.
    subtitle = RssEntryFeed.description		# Use the description of the RSS feed for this root tag.

    
    def __call__(self, request, *args, **kwargs):
        """Place for intercepting the call to the custom Atom feed, and perform
        pre-processing checks.
        """
        # Only authenticated users can view the feed.
        if not request.user.is_authenticated():
            return HttpResponseForbidden("<h3>Access Forbidden. User must be authenicated to access page.</h3>")
        else:
            return super(AtomEntryFeed, self).__call__(request, *args, **kwargs)

       
    def item_extra_kwargs(self, item):
        """
        Returns an extra keyword arguments dictionary that is used with
        the `add_item` call of the feed generator.
        Add the 'content' field of the 'Entry' item, to be used by the custom feed generator.
        """
        return { 'content': item.content, }
        '''