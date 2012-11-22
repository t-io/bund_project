from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Get access to the Models
from bundproject.geography.models import Location
from bundproject.geography.models import Road

# Create your views here.



def landing(request):
    """ Shows the LandingPage, Site is for Public Viewing """

    headline = "Bund Project"

    points = Location.objects.order_by('name')
    lines = Road.objects.order_by('name')

    '''
    print "Points: "
    for p in points:
    	print p.name
    '''

    print "\n\nLines: "
    for l in lines:
        print "\n",l
        print "LinePoints"
        for x, y in l.line:
            print "X: ", x, " Y: ", y



    return render_to_response('landing.html', {
                                        'headline': headline,
                                        'all_points' : points,
                                        'all_lines' : lines
                                        },
                                        context_instance = RequestContext(request)
                                    )