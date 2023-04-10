import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from places.models import Place, Image


def home(request):
    places = Place.objects.all()
    places_dict = {
        "type": "FeatureCollection",
        "features": []
    }

    for p in places:
        images = Image.objects.filter(place=p.pk)
        p_dict = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [p.lng, p.lat]
            },
            "properties": {
                "title": p.title_map,
                "placeId": p.pk,
                "title_text": p.title_text,
                "imgs": [img.image.url for img in images],
                "short_description": p.description_short,
                "long_description": p.description_long,
            }
        }
        places_dict["features"].append(p_dict)
    return render(request, 'index.html', {"places_dict": places_dict})


def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = Image.objects.filter(place=place.pk)
    place_dict = {
        "title": place.title_text,
        "imgs": [img.image.url for img in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": str(place.lng),
            "lat": str(place.lat)
        }
    }
    place_json = json.dumps(place_dict, ensure_ascii=False, indent=4)
    return HttpResponse(place_json, content_type='application/json; charset=utf-8')
