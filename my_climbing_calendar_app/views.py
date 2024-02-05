from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Day
from .forms import DayForm
from django.http import HttpResponseRedirect

class DayListView(ListView):
    model = Day
    template_name = 'my_climbing_calendar_app/day_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['days'] = context['object_list']
        return context

class DayCreateView(CreateView):
    model = Day
    form_class = DayForm
    template_name = 'my_climbing_calendar_app/day_form.html'
    success_url = reverse_lazy('day_list')

class DayUpdateView(UpdateView):
    model = Day
    form_class = DayForm
    template_name = 'my_climbing_calendar_app/day_form.html'
    success_url = reverse_lazy('day_list')

class DayDeleteView(DeleteView):
    model = Day
    success_url = reverse_lazy('day_list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())



