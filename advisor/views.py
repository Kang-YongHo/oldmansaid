from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import MyModel
from .forms import MyModelForm

class MyModelListView(ListView):
    model = MyModel
    template_name = 'advisor/index.html'
    context_object_name = 'items'

class MyModelCreateView(CreateView):
    model = MyModel
    form_class = MyModelForm
    template_name = 'advisor/form.html'
    success_url = reverse_lazy('index')

class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'advisor/detail.html'
    context_object_name = 'item'

class MyModelUpdateView(UpdateView):
    model = MyModel
    form_class = MyModelForm
    template_name = 'advisor/form.html'
    success_url = reverse_lazy('index')

class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'advisor/confirm_delete.html'
    success_url = reverse_lazy('index')
