# -*- coding: utf-8 -*-

import pandas as pd
from django.shortcuts import render, redirect
from course.models import Course
from .forms import UploadFileForm
import os
from django.conf import settings

def handle_uploaded_file(f):
    file_path = os.path.join(settings.MEDIA_ROOT, f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def is_excel_file(file_name):
    # ?��? ?�일 ?�장???�인
    valid_extensions = ['.xlsx', '.xls']
    file_ext = os.path.splitext(file_name)[1]
    return file_ext.lower() in valid_extensions

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if is_excel_file(file.name):
                file_path = handle_uploaded_file(file)
                
                # ?�일 ?�장?�에 ?�라 ?�절???�진??지??
                file_ext = os.path.splitext(file.name)[1]
                engine = 'openpyxl' if file_ext == '.xlsx' else 'xlrd'
                
                # ?��? ?�일??Pandas�??�어?�기
                try:
                    df = pd.read_excel(file_path, engine=engine)
                    for _, row in df.iterrows():
                        Course.objects.create(
                            course_id=row['?학수번호-분반'],
                            course_name=row['과목명'],
                            instructor=row['교수명'],
                            credits=row['학점'],
                            classification=row['이수구분'],
                            course_week=row['요일'],
                            course_period=row['교시'],
                            course_room=row['장소'],
                        )
                    return redirect('upload_success')
                except pd.errors.ParserError as e:
                    return render(request, 'course_table/upload.html', {
                        'form': form,
                        'error': '?��? ?�일???�어?�는 �??�류가 발생?�습?�다.'
                    })
            else:
                return render(request, 'course_table/upload.html', {
                    'form': form,
                    'error': '지?�하지 ?�는 ?�일 ?�식?�니?? ?��? ?�일(.xlsx, .xls)???�로?�해주세??'
                })
    else:
        form = UploadFileForm()
    return render(request, 'course_table/upload.html', {'form': form})

def home(request):
    return render(request, 'course_table/home.html')
