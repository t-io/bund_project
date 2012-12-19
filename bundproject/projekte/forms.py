# -*- coding: utf-8 -*-
from django import forms
from bundproject.projekte.models import Road

import floppyforms as forms



class SearchForm(forms.Form):
    """Search Model by values"""

    PLANUNSSTD = (
        ('', '- Leere Auswahl -'),
        ('Vorplanung', 'Vorplanung'),
        ('Raumordnungsverfahren', 'Raumordnungsverfahren'),
        ('Raumordnungsverfahren abgeschlossen', 'Raumordnungsverfahren abgeschlossen'),
        ('Linienbestimmung', 'Linienbestimmung'),
        ('Linienbestimmt', 'Linienbestimmt'),
        ('Planfeststellungsverfahren', 'Planfeststellungsverfahren'),
        ('Planfestgestellt', 'Planfestgestellt'),
    )

    name = forms.CharField(widget=forms.TextInput, required=False, label='', max_length=200)
    name.attrs={'class': 'searchfield'}   

    art = forms.CharField(widget=forms.Select(choices=(('', '- Leere Auswahl -'),('AU','Autobahn'),('BU','Bundesstraße'))), required=False, label='', max_length=200)
    art.attrs={'class': 'searchfield'}  

    projekt_typ = forms.CharField(widget=forms.Select(choices=(('', '- Leere Auswahl -'),('A','Ausbau'),('N','Neubau'))), required=False, label='', max_length=200)
    projekt_typ.attrs={'class': 'searchfield'}  

    kosten = forms.CharField(widget=forms.TextInput, required=False, label='', max_length=200)
    kosten.attrs={'class': 'searchfield'}  

    bedarf = forms.CharField(widget=forms.Select(choices=(('', '- Leere Auswahl -'),('VB','vordringlicher Bedarf'),('WB','weiterer Bedarf'),('KB','kein Bedarf'))), required=False, label='', max_length=200)
    bedarf.attrs={'class': 'searchfield'}  

    planungsstand = forms.CharField(widget=forms.Select(choices=PLANUNSSTD), required=False, label='', max_length=200)
    planungsstand.attrs={'class': 'searchfield'}

    #forms.Select(choices=PLANUNSSTD)

    def build_queryset(self):
        '''
        Searches a given QuerySet and returns a
        QuerySet that contains any word in the list of keywords
        '''

        query = Road.objects.all()

        if (self.cleaned_data['name'] and self.cleaned_data['name'] != ''):
            query = query.filter(name__icontains = self.cleaned_data['name'])
       
        
        if (self.cleaned_data['art'] is not None and self.cleaned_data['art'] != ''):
            query = query.filter(art__icontains = self.cleaned_data['art'])

        if (self.cleaned_data['projekt_typ'] is not None and self.cleaned_data['projekt_typ'] != ''):
            query = query.filter(projekt_typ__icontains = self.cleaned_data['projekt_typ'])


        if (self.cleaned_data['kosten'] is not None and self.cleaned_data['kosten'] != ''):
            query = query.filter(kosten__icontains = self.cleaned_data['kosten'])

        if (self.cleaned_data['bedarf'] is not None and self.cleaned_data['bedarf'] != ''):
            query = query.filter(bedarf__icontains = self.cleaned_data['bedarf'])


        if (self.cleaned_data['planungsstand'] is not None and self.cleaned_data['planungsstand'] != ''):
            query = query.filter(planungsstand__icontains = self.cleaned_data['planungsstand'])


        return query


    def requestInfo(self):
        if(self.cleaned_data['name'] == '' and self.cleaned_data['art'] == '' 
        and self.cleaned_data['projekt_typ'] == '' and self.cleaned_data['kosten'] == '' 
        and self.cleaned_data['bedarf'] == '' and self.cleaned_data['planungsstand']== '' ):

            return True;
        else:
            return False;


class LineWidget(forms.gis.LineStringWidget, forms.gis.BaseGMapWidget):
    map_width = 690
    map_height = 300



'''
class GeoForm(forms.Form):
    my_line = forms.gis.LineStringField()
'''




class GeoForm(forms.ModelForm):
    class Meta:
        model = Road
        widgets = {

            'line': LineWidget(),
        }











