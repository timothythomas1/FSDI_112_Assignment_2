from django.views.generic import TemplateView # TemplateView retrievs templates

class HomePageView(TemplateView): # Instantiates a new TemplateView class
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"