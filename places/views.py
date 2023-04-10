from django.shortcuts import render

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
