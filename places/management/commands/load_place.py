import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from transliterate import slugify
from places.models import Place, Image


def get_json(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_raw_image(image_urls):
    for image_url in image_urls:
        response = requests.get(image_url)
        response.raise_for_status()
        name = image_url.split('/')[-1]
        yield name, response.content


def create_place(json_url):
    json = get_json(json_url)
    image_urls = json['imgs']
    
    place_object, is_created = Place.objects.get_or_create(
                title=json['title'],
                slug=slugify(json['title']),
                description_short=json['description_short'],
                description_long=json['description_long'],
                latitude=json['coordinates']['lat'],
                longitude=json['coordinates']['lng'],
            )

    if not is_created:
        return

    for image in get_raw_image(image_urls):
        name, content = image
        image_object = Image.objects.create(place=place_object)
        image_object.image.save(name, ContentFile(content), save=True)


class Command(BaseCommand):
    help = 'Load places from JSON files to database'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):
        for url in options['url']:
            create_place(url)
