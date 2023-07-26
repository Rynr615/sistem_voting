from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Polling, Choice

# Get polls and display them
def index(request):
    latest_polling_list = Polling.objects.order_by('-pub_date')[:5]
    context = {'latest_polling_list': latest_polling_list}
    return render(request, 'polls/index.html', context)

# Show specific poll and choices
def detail(request, polling_id):
    try:
        polling = Polling.objects.get(pk=polling_id)
    except Polling.DoesNotExist:
        raise Http404("Polling does not exist")
    return render(request, 'polls/detail.html', {'polling': polling})

# Get poll and display results
def results(request, polling_id):
    polling = get_object_or_404(Polling, pk=polling_id)
    return render(request, 'polls/results.html', {'polling': polling})

# views.py

def has_voted(request, polling_id):
    return request.COOKIES.get('voted_polling_{}'.format(polling_id), False)


# views.py
# views.py

@login_required
def vote(request, polling_id):
    polling = get_object_or_404(Polling, pk=polling_id)
    if has_voted(request, polling_id):
        return render(request, 'polls/detail.html', {
            'polling': polling,
            'error_message': "You have already voted for this polling.",
        })
    try:
        selected_choice = polling.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'polling': polling,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Set session to mark that the user has voted for this polling.
        request.session['voted_polling_{}'.format(polling_id)] = True
        return HttpResponseRedirect(reverse('polls:results', args=(polling.id,)))



