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
from django.contrib.auth.models import User


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
    paginator = Paginator(lines, 20) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)


    return render_to_response('landing.html', {
                                        'filter_headline': filter_headline,
                                      	'searchform': searchForm,
                                        'show_lines' : show_lines
                                        },
                                        context_instance = RequestContext(request)
                                    )


@login_required
def add_road(request, slug_name=None):
    
    
    if slug_name:    
        headline = "Straße bearbeiten"
        road = get_object_or_404(Road, slug = slug_name)
        
        if road.erstellt_von != request.user:
            raise HttpResponseForbidden()

        form = GeoForm(data=request.POST or None, instance=road)

    else:
        form = GeoForm(request.POST or None)
        headline = "Straße anlegen"

    if request.POST:

        '''
        Eingabe ist nicht OK
        '''

        # wenn eingaben ok
        if form.is_valid():
            form.instance.erstellt_von = User.objects.get( username = request.user.username )
            cmodel = form.save()
            cmodel.save()
            return redirect(landing)
    

    return render_to_response('add.html', {
                                            'headline': headline,
                                            'form': form
                                            },
                              context_instance=RequestContext(request))

def edit_road(request, slug_name):

    road = get_object_or_404(Road, slug = slug_name)
    form = GeoForm(data=request.POST or None, instance=road)
    headline = "Straße bearbeiten"

    if request.method == 'POST':
        if form.is_valid():
            cmodel = form.save()
            cmodel.save()
            print "Valid"
            return redirect('landing')
        else:
            print "Not Valid"



    return render_to_response('add.html', {
                                            'headline': headline,
                                            'form': form
                                        },
                              context_instance=RequestContext(request))

def details(request, slug_name):
    #Detailansicht einer einzelnen Strasse
    entry = get_object_or_404(Road, slug = slug_name)
    
    return render_to_response('details.html', { 'road' : entry },
                          context_instance=RequestContext(request))


















