# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.db import models
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Choice, Poll
from django.template import RequestContext, loader

# Create your views here.

def inicio(request):
    titulo = "Menú de Preguntas"
    return render(request, 'polls/menu.html', {'titulo':titulo})

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

