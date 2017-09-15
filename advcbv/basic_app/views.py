from django.shortcuts import render
from django.views.generic import View, TemplateView


# Create your views here.
#def index(request):
#    return render(request, 'index.html')

#class CBView(View):
#    def get(self, request):
#        return HttpResponse("Hello World!")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # creating context dictionary
        context['injectme'] = "basic injection"     # now storing key-value pair in dictionary
        return context
