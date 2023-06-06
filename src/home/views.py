from django.views import generic

# Create your views here.

# Home page

class HomePage (generic.TemplateView):
    template_name = "home_page.html"