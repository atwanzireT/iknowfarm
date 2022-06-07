from django.shortcuts import render

# Create your views here.
def CSVupload(request):
    return render(request, 'farmercsv.html', {})

def VideoUploads(request):
    dic = {}
    return render(request, "video.html", dic)