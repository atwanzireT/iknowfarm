import imp
from django.shortcuts import render
from pyparsing import line
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import *
from django.core.paginator import Paginator
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, landscape


# Create your views here.
def district(request):
    villages = Village.objects.all()
    dic = {
        'villages':villages,
    }
    return render(request, 'districts.html', dic)


def farmer_groups(request):
    farmer_groups = Farmer.objects.filter(registrationtype=2)
    dic = {
        'farmer_groups':farmer_groups,
    }
    return render(request, 'farmergroups.html', dic)

def farmer(request):
    farmers = Farmer.objects.all()

    paginator = Paginator(farmers, 5)
    page = request.GET.get('page')
    farmers = paginator.get_page(page)
    dic = {
        'farmers':farmers,
    }
    return render(request, 'farmer_list.html', dic)

class UpdateFarmerView(LoginRequiredMixin, generic.UpdateView):
    model = Farmer
    template_name = 'editFarmer.html'
    form_class = FarmerForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['farmers'] = Farmer.objects.all()
        return context

class AddFarmerView(LoginRequiredMixin, generic.CreateView):
    model = Farmer
    template_name = 'addFarmer.html'
    form_class = FarmerForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['farmers'] = Farmer.objects.all()
        return context

def farmer_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    farmers = Farmer.objects.all()
    lines = []
    for farmer in farmers:
        lines.append(farmer.id)

    p.drawString(100, 100, lines)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='farmer.pdf')