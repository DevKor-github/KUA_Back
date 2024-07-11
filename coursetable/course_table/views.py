import pandas as pd
from django.shortcuts import render, redirect
from .models import Course
from .forms import UploadFileForm

def home(request):
    return render(request, 'course_table/home.html')

def handle_uploaded_file(f):
    df = pd.read_excel(f)
    for index, row in df.iterrows():
        Course.objects.create(
            course_id=row['학수번호-분반'],
            course_name=row['과목명'],
            instructor=row['교수명'],
            credits=row['학점'],
            classification=row['이수구분'],
            course_week=row['요일'],
            course_period=row['교시'],
            course_room=row['장소'],

        )
        
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'course_table/upload.html', {'form': form})
