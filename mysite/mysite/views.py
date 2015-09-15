import datetime
from django.template import Context
from django.http import HttpResponse, HttpRequest
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from licence.models import licence_model
l = licence_model.objects.all()
l.delete()

""""def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)
	"""
def current_datetime(request):
	current_date = datetime.datetime.now()
	return render_to_response('current_datetime.html', locals())

"""def current_datetime(request):
	if request.method == 'POST':
	current_date = datetime.datetime.now()
	return render_to_response('current_datetime.html', locals())
"""
	#html = "<html><body>It is now %s.</body></html>" % now
	#return HttpResponse(html)
	
def hours_ahead(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

@csrf_exempt
def licence(request):
	#sys_time = datetime.datetime.now()
	if request.method == 'POST':
		#html = "<html><body>GOTCHA</body></html>"
		#html = "<html><body>testing the element</body></html>"
		#name = HttpRequest.body
		name = HttpRequest.readline(request)
		pc_time = datetime.datetime.now()
		l = licence_model(number = name, timestamp = pc_time)
		l.save()
		#p = licence_model.objects.all()
		#p.delete()
		#p.save()
		l.delete
		#print p.number
		#stamp = p.timestamp
		#print q
		#print licence_model.objects.all()
		#return HttpResponse(html)
		return render_to_response('licence_post.html', locals())
		#licence_model.delete()
		#l.delete()
	elif request.method == 'GET':
		#html = "<html><body>testing the GET</body></html>"
		#getdata = licence_model.objects.all()
		list = licence_model.objects.all()
		#getstamp = list.order_by("timestamp")
		#getno = list.order_by("timestamp")
		#list.delete()
		#print licence_model.objects.all()[0]
		#actual_time = l.timestamp
		#name = request.GET.get('datasent', None)
		#html = "<html><body> %s</body></html>" % name
	#return HttpResponse(html)
		#list.delete()
		#print 'eimai'
		return render_to_response('licence_time.html', locals())	