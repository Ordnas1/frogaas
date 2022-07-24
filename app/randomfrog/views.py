from django.http import FileResponse
from core.models import Frog


def random(response):
    """Return random frog"""
    random_frog = Frog.objects.order_by('?')[0]
    print(random_frog)
    img = open(random_frog.image.path, 'rb')

    return FileResponse(img)
