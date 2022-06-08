from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib import messages
  
# Create your views here.
def feedback(request):
    if request.method == 'POST': # check post
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = Feedback() #create relation with model # get form input data
            data = form.save(commit=False)
            data.user = request.user
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            messages.success(request,"Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/feedback/feedback')

    form = FeedbackForm
    context={'form':form,}
    return render(request, 'feedback.html', context)