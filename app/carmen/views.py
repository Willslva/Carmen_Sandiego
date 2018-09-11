
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models
from django.db.models import Max
import random
from .forms import UUIDUserForm
from django.http import HttpResponseRedirect

class UserCreateView(CreateView):
    model = models.UUIDUser
    template_name = 'user/form.html'
    success_url = reverse_lazy('carmen:login')
    form_class = UUIDUserForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return super(UserCreateView, self).form_valid(form)

class PartidaCreate(CreateView):
    model = models.Partida
    template_name = 'core/criarpartida.html'
    success_url = reverse_lazy('forca:game')
    fields = ['fase']

    def form_valid(self, form):
        if (models.Partida.objects.filter(usuario=self.request.user)):
            return HttpResponseRedirect('/jogo/')
        else:
            obj = form.save(commit=False)
            obj.usuario = self.request.user
            obj.save()
            return super(PartidaCreate, self).form_valid(form)

class Game(ListView):
    model = models.Partida
    template_name = 'core/jogo.html'

    def get_context_data(self, **kwargs):
        kwargs['partida'] = models.Partida.objects.all()
        return super(Game, self).get_context_data(**kwargs)


class Jogo(TemplateView):
    template_name = 'core/home.html'

class Fase1(TemplateView):
    template_name = 'core/pequim.html'

class Testemunhas1(TemplateView):
    template_name = 'core/testemunhaspequim.html'

class Fase2(TemplateView):
    template_name = 'core/paris.html'

class Testemunhas2(TemplateView):
    template_name = 'core/testemunhasparis.html'

class Fase3(TemplateView):
    template_name = 'core/bogota.html'

class Testemunhas3(TemplateView):
    template_name = 'core/testemunhasbogota.html'

class Fase4(TemplateView):
    template_name = 'core/buenosaires.html'

class Testemunhas4(TemplateView):
    template_name = 'core/testemunhasbuenosaires.html'

class Mapa (TemplateView):
    template_name = 'core/mapapequim.html'

class MapaMundi (TemplateView):
    template_name = 'core/mapa.html'

