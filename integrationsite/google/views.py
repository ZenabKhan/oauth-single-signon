from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('google/index.html')
    context = {
        'logged_in': request.user.is_authenticated,
    }
    return HttpResponse(template.render(context, request))
