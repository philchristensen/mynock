from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from mynock.feeds.models import FeedItem

def summary(request):
	result = FeedItem.objects.order_by('-download_date').all()
	paginator = Paginator(result, 10)
	
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	
	try:
		recent_torrents = paginator.page(page)
	except (EmptyPage, InvalidPage):
		recent_torrents = paginator.page(paginator.num_pages)
	
	return render_to_response('summary.html', dict(
		recent_torrents		= recent_torrents,
	), context_instance=RequestContext(request))