# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Get access to the Models
from bundproject.projekte.models import Location
from bundproject.projekte.models import Road

from bundproject.projekte.forms import SearchForm
from bundproject.projekte.forms import GeoForm


def landing(request):
    """ Shows the LandingPage, Site is for Public Viewing """

    filter_headline = "Alle Datensätze"

    lines = Road.objects.order_by('name')

    searchForm = SearchForm(request.POST)

    if request.method == 'POST':
        if searchForm.is_valid():
            lines = searchForm.build_queryset()

            if( searchForm.requestInfo() ):
            	filter_headline = "Alle Datensätze"
            else:
            	filter_headline = "Gefilterte Datensätze"

    """	Django Pagination	"""
    paginator = Paginator(lines, 1) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)




    '''
    print "\n\nLines: "
    for l in lines:
        print "\n",l
        print "LinePoints"
        for x, y in l.line:
            print "X: ", x, " Y: ", y
    
    print filter_headline
    print "RequestInfo: ", searchForm.requestInfo()
    '''
    

    return render_to_response('landing.html', {
                                        'filter_headline': filter_headline,
                                      	'searchform': searchForm,
                                        'show_lines' : show_lines
                                        },
                                        context_instance = RequestContext(request)
                                    )


#neuer Eintrag
def add_road(request):
    # sticks in a POST or renders empty form
    form = GeoForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
        return redirect(landing)
    

    return render_to_response('add.html', {'form': form},
                              context_instance=RequestContext(request))


