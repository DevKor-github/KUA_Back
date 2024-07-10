import pandas as pd
from django.shortcuts import render
from .models import MyModel
from .forms import UploadFileForm

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                MyModel.objects.create(
                    field1=row['field1'],
                    field2=row['field2'],
                    field3=row['field3']
                )
            return render(request, 'myapp/upload_success.html')
    else:
        form = UploadFileForm()
    return render(request, 'myapp/upload.html', {'form': form})
