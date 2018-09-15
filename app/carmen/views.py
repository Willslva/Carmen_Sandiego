
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models
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
    fields = ['fase', 'verificador']

    def form_valid(self, form):
        if (models.Partida.objects.filter(usuario=self.request.user)):
            return HttpResponseRedirect('/game/')  
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

    def get_queryset(self):
        if ('a' in self.request.POST):
            models.Partida.objects.filter(usuario=self.request.user.id).update(fase=1) 
        elif ('b' in self.request.POST):
            models.Partida.objects.filter(usuario=self.request.user.id).update(fase=2)
        elif ('c' in self.request.POST):
            models.Partida.objects.filter(usuario=self.request.user.id).update(fase=3)
        elif ('d' in self.request.POST):
            models.Partida.objects.filter(usuario=self.request.user.id).update(fase=4)
        elif ('e' in self.request.POST):
            models.Partida.objects.filter(usuario=self.request.user.id).update(fase=5)
        elif ('f' in self.request.POST):
            models.Partida.objects.filter(usuario=self.request.user.id).update(fase=6)

    def post(self, request, *args, **kwargs):
        if ('a' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('b' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('c' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('d' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('e' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('f' in self.request.POST):
            return self.get(request, *args, **kwargs)


class Jogo(TemplateView):
    template_name = 'core/home.html'

class Sobre(TemplateView):
    template_name = 'core/sobre.html'

class Intro(ListView):
    model = models.Partida
    template_name = 'core/introducao.html'

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

class Fase5(TemplateView):
    template_name = 'core/atenas.html'

class Testemunhas5(TemplateView):
    template_name = 'core/testemunhasatenas.html'

class Fase6(TemplateView):
    template_name = 'core/sydney.html'

class Testemunhas6(TemplateView):
    template_name = 'core/testemunhassydney.html'

class Fase7(TemplateView):
    template_name = 'core/sandiego.html'

class Testemunhas7(TemplateView):
    template_name = 'core/testemunhassandiego.html'

class Mapa (TemplateView):
    template_name = 'core/mapapequim.html'

class MapaMundi (TemplateView):
    template_name = 'core/mapa.html'

class Home (TemplateView):
    template_name = "core/home.html"
