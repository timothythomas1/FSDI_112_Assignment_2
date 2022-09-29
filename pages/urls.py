from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # "name" tags are used for the anchor tags
    path('about/', AboutPageView.as_view(), name='about'), # "name" tags are used for the anchor tags

]