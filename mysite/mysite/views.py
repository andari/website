import datetime
from django.template import Context
from django.http import HttpResponse, HttpRequest
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from licence.models import licence_model

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
		#print name
		#licence_model.objects.all()
		p = licence_model(licence_number = name)
		p.save()
		print p
		q = licence_model(scan_time = pc_time )
		q.save()
		print q
		#return HttpResponse(html)
		return render_to_response('licence_time.html', locals())
	elif request.method == 'GET':
		#html = "<html><body>testing the GET</body></html>"
		#getdata = licence_model.objects.all()
		getdata = licence_model.objects.all()
		actual_time = licence_model.objects.all()
		#name = request.GET.get('datasent', None)
		#html = "<html><body> %s</body></html>" % name
	#return HttpResponse(html)
		return render_to_response('licence_time.html', locals())
		getdata.delete()	