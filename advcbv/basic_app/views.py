from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import (View, TemplateView,ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from . import models

# Create your views here.
#def index(request):
#    return render(request, 'index.html')

#class CBView(View):
#    def get(self, request):
#        return HttpResponse("Hello World!")

# Template view
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # creating context dictionary
        context['injectme'] = "basic injection"     # now storing key-value pair in dictionary
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'  # default : modelName.lower()_list, Eg: school_list
    # queryset = School.objects.all() ---> can be used for getting specific information.
    # we can use get_queryset() method for dynamic filtering. Check docs.
    model = models.School  # shorthand of "queryset = School.objects.all()". refer documentation
    # We can use "template_name" to specify template name, default: modelName.lower()_list.html 
    
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'  # default : modelName.lower(), Eg: school
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')




