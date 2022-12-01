from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return  render(request , "index.html")

def handelform(request):
    if request.method == "POST" and request.FILES['company'] and request.FILES['new']:
        new_csv =   request.FILES['new']
        company = request.FILES['company']
        fss = FileSystemStorage()
        file = fss.save("train_data.csv", company)
        file2 = fss.save("test_data.csv", new_csv)
        return render(request , "handel.html")