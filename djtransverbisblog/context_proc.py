from djtransverbisblog.models import Page, Comment
from django.conf import settings


def base_variables(request):
    return {'pages': Page.objects.filter(sidebar=False).order_by('page_order'),
            'sidebar': Page.objects.filter(sidebar=True).first(),
            'newcomms': len(Comment.objects.filter(approved_comment=False)),
            'website_name': settings.WEBSITE_NAME,
            'website_slogan': settings.WEBSITE_SLOGAN}
