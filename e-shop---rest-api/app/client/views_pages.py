from django.http import HttpResponse
from django.template import loader


# PUBLIC VIEWS
def indexPage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))
