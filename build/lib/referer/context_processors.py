from . import settings
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

if hasattr(settings, 'REFERER_MODEL_FROM') and hasattr(settings, 'REFERER_MODEL_IMPORT'):
    Referer = getattr(__import__(settings.REFERER_MODEL_FROM, fromlist=[settings.REFERER_MODEL_IMPORT]), settings.REFERER_MODEL_IMPORT)
else:
    from django.contrib.auth.models import User as Referer


def get_referer(refererID):
    try:
        return Referer.objects.get(id=refererID)
    except (ValueError, ObjectDoesNotExist):
        return get_referer(settings.REFERER_DEFAULT_ID)


def referer(request):
    refererID = request.GET.get(settings.REFERER_LINK_PARAMETER, '')
    refererObject = get_referer(refererID)
    return {"referer": refererObject}
