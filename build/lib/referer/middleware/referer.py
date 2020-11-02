from .. import settings
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class RefererMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        if (
            any(
                path in request.META.get('PATH_INFO')
                for path in settings.REFERER_IGNORED_LINKS
            )
            or not request.META.get('HTTP_REFERER')
            or f'{settings.REFERER_LINK_PARAMETER}='
            not in request.META.get('HTTP_REFERER')
            or request.GET.get(settings.REFERER_LINK_PARAMETER, '')
        ):
            return
        refererID = request.META.get('HTTP_REFERER').split('=')[-1]
        queryConnection = '&' if request.META.get('QUERY_STRING') else ''
        queryString = f"{request.META.get('QUERY_STRING')}{queryConnection}{settings.REFERER_LINK_PARAMETER}={refererID}"
        return HttpResponseRedirect(f"{request.META.get('PATH_INFO')}?{queryString}")
