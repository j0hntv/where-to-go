from django.shortcuts import render
from places.models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                'type': 'Feature',
                'geometry': {'type': 'Point', 'coordinates': [place.longitude, place.latitude]},
                'properties': {'title': place.title, 'placeId': place.slug, 'detailsUrl': ''}
            }
        )
        
    context = {
        'places_geojson': {
            'type': 'FeatureCollection',
            'features': features
        }
        
    }

    return render(request, 'index.html', context)
