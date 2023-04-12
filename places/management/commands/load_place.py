import requests
from io import BytesIO

from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = "Method for uploading json data with places"

    def add_arguments(self, parser):
        parser.add_argument(
            "path",
            type=str
        )

    def handle(self, *args, **options):
        response = requests.get(options["path"])
        if response.status_code >= 400:
            print(f"Data not found by url {options['path']}!")
            return

        data_json = response.json()
        places = Place.objects.filter(title_text=data_json["title"])
        if len(places) > 0:
            print(f"Place with title {data_json['title']} already exists!")
            return

        place = Place(
            title_text=data_json["title"],
            title_map=data_json["title"],
            description_short=data_json["description_short"],
            description_long=data_json["description_long"],
            lng=data_json["coordinates"]["lng"],
            lat=data_json["coordinates"]["lat"],
        )
        place.save()
        print("Place created!")

        for path in data_json["imgs"]:
            img_name = path.split("/")[-1]
            response = requests.get(path)
            image_obj = BytesIO(response.content)
            image = Image(
                place=place
            )
            image.image.save(img_name, image_obj, save=False)
            image.save()
        print("All photos uploaded!")
