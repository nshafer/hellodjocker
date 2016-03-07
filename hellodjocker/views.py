import os

from django.core.cache import cache
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView, CreateView

from guestbook.models import Signature


class HomeView(CreateView):
    model = Signature
    fields = ('name',)
    template_name = "home.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        try:
            visits = cache.incr('visits')
        except ValueError:
            cache.set('visits', 1)
            visits = 1

        context = {
            'name': os.getenv("NAME", "World"),
            'environment': os.environ,
            'signatures': Signature.objects.all().order_by("-added"),
            'visits': visits,
        }
        context.update(kwargs)
        return super().get_context_data(**context)

