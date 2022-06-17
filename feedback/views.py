from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib import messages
from django.core.paginator import Paginator
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

  
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

class ReplyView(LoginRequiredMixin, generic.UpdateView):
    model = Feedback
    template_name = 'editfeed.html'
    form_class = FeedbackForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['feedback'] = Feedback.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse_lazy('feedback')