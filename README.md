## rss tutor

BELOW: 	
------

    def search_result(request)

        rssfeed=''
        if search and not city:rssfeed+=search
        
        .......
        return render_to_response({'rsskey':rssfeed.....
        
        

### tagging/templates/registration/searchresult.html 

#### BELOW: 

`<div style="border:1px solid yellow;width:890px;"><table><tr><td>{% if details %}`

::
    
    {% if rsskey %}
    <span><a href='/feeds/tag/{{ rsskey }}' target="_blank" >
    <img src="http://feedicons.com/images/feed-icon-14x14.png">
    Subscribe to this feed in your RSS Reader</a></span>
    {% endif %}
	<!--/-->
	

#### urls.py

BELOW: urlpatterns = patterns(''
--------------------------------

::

    url(r'^feeds/tag/(?P<bits>.*)/$', 'registration.views.rss201'),
	


registration/views.py
---------------------

on top:
	
	from django.http import HttpResponse,Http404

	def rss201(request,bits):
	    from django.utils.feedgenerator import Rss201rev2Feed
	    query = Q(key_skills__icontains=bits ) | Q(title__icontains=bits )
	    try:
	        object_list = jobs.objects.filter(query)
	    except:# Tag.DocumentDoesNotExist:
	        raise Http404
	
	    feedtitle=u"Showing the RSS Feeds on %s" % bits
	    site_link = u'http://italent.com/'
	    feed = Rss201rev2Feed( title=u"Italents Job Search.com",
	        link=site_link,
	        description=feedtitle,
	        language=u"en")
	
	    for object in object_list:        
	        link = site_link + unicode(object.id)
	        desc = u"Job Summary: %s, Key Skills: %s, City: %s, Salary: %d, Qualification: %s" % (object.jobsummary, object.key_skills, 
	            object.city, object.min_salary, object.qualification)
	        feed.add_item( title=object.title, link=link,
	            description=desc)
	    response = HttpResponse(mimetype='application/xml')
	    feed.write(response, 'utf-8')
	    return response
	

