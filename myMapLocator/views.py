from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Viewmap
from django.views.generic import TemplateView
from .forms import Viewform
import folium
import geocoder
from geopy.geocoders import Nominatim



#Map 1
def baseview(request):
    form = Viewform()
    if request.method == 'POST':
        form = Viewform(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = Viewform()
    address = Viewmap.objects.all().last()
    location = geocoder.osm(address)
    #locator = Nominatim(user_agent='myMap')
    #location = locator.geocode(address)
    #lat = location.latitude
    #lng = location.longitude
    lat = 6.4532
    lng = 3.2345
    country = location.country
    if lat == None or lng == None:
        return HttpResponse('You address input is invalid')

    else:
        m = folium.Map(location=[19.1235, -12.1519], zoom_start=2)

        folium.Marker([lat, lng], tooltip='Click for more',
                      popup=country).add_to(m)

        m = m._repr_html_()

    return render(request, 'base.html', {'m': m, 'form': form})


#Map 2
class FoliumView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        figure = folium.Figure()
        m = folium.Map(
            location=[6.465422, 3.406448],
            zoom_start=8,
            tiles='Stamen Terrain'
        )
        m.add_to(figure)

        folium.Marker(
            location=[6.4698, 3.601521],
            popup='Lekki Lagos',
            tooltip='Click for more',
            icon=folium.Icon(icon='cloud')
        ).add_to(m)

        folium.Marker(
            location=[9.0479, 7.5155],
            popup='Asokoro Abuja',
            tooltip='Click for more',
            icon=folium.Icon(color='green')
        ).add_to(m)

        folium.Marker(
            location=[6.4667, 3.4500],
            popup='Banana Island, Lagos',
            tooltip='Click for more',
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
        figure.render()
        return {"map": figure}
