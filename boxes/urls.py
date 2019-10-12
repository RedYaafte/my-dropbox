from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views import box_list, box_detail


urlpatterns = [
    path('box/', box_list),
    path('box/<int:pk>/', box_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
