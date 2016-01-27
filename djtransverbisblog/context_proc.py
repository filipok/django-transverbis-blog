from djtransverbisblog.models import Page, Comment


def base_variables(request):
    return {'pages': Page.objects.filter(sidebar=False).order_by('page_order'),
            'sidebar': Page.objects.filter(sidebar=True).first(),
            'newcomms': len(Comment.objects.filter(approved_comment=False))}
