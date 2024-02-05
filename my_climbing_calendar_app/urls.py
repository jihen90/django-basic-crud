from django.urls import path
from .views import DayListView, DayCreateView, DayUpdateView, DayDeleteView

urlpatterns = [
    path('days/', DayListView.as_view(), name='day_list'),
    path('days/new/', DayCreateView.as_view(), name='day_new'),
    path('days/<int:pk>/edit/', DayUpdateView.as_view(), name='day_edit'),
    path('days/<int:pk>/delete/', DayDeleteView.as_view(), name='day_delete'),
]
