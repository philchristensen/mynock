from django.shortcuts import render_to_response
from django.template import RequestContext

from mynock.feeds.models import FeedItem

def summary(request):
	recent_torrents = FeedItem.objects.order_by('-download_date')[:10]
	
	return render_to_response('summary.html', dict(
		recent_torrents	= recent_torrents,
	), context_instance=RequestContext(request))