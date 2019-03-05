from django.views.generic import TemplateView

class HomePage(TemplateView):
    text_var = 'This is my fouth django app web page'
    template_name = 'index.html'
