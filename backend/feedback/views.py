from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib import messages
from django.core.paginator import Paginator
  
# Create your views here.
def feedback(request):
    feedback = Feedback.objects.all()

    # feedback pagination
    paginator = Paginator(feedback, 5)
    page = request.GET.get('page')
    feedback = paginator.get_page(page)
    dic= {
        'feedback': feedback,
    }
    return render(request, 'feeds.html', dic)