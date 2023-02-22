from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .utils.DnDtool import generate2


from .models import RuinName, Choice, RuinedPlaces

def index(request):
    latest_ruinName_list = RuinName.objects.order_by('-pub_date')[:5]
    context = {'latest_ruinName_list': latest_ruinName_list}
    return render(request, 'ruinGen/index.html', context)

def detail(request, ruinName_id):
    ruin = get_object_or_404(RuinName, pk=ruinName_id)
    return render(request, 'ruinGen/detail.html', {'ruin': ruin})

def results(request, ruinName_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % ruinName_id)

def vote(request, ruinName_id):
    ruin = get_object_or_404(RuinName, pk=ruinName_id)
    try:
        selected_choice = ruin.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'ruinGen/detail.html', {
            'ruin': ruin,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('ruinGen:results', args=(ruin.id,)))

def ruinBuild(request):
    result = generate2()
    context = {'result': result}
    return render(request, 'ruinGen/ruinBuild.html', context)