from django.db import models

# Create your models here.
def CSVupload(request):
    return render(request, 'farmercsv.html', {})
