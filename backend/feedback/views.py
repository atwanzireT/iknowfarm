from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib import messages
  
# Create your views here.
def contact(request):
    if request.method == 'POST': # check post
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = Feedback() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            messages.success(request,"Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contact/')

    form = FeedbackForm
    context={'form':form,}
    return render(request, 'contact.html', context)