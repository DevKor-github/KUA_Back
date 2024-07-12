import pandas as pd
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from .models import Course
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'instructor', 'credits')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-excel/', self.admin_site.admin_view(self.upload_excel), name='upload-excel'),
        ]
        return custom_urls + urls

    def upload_excel(self, request):
        if request.method == "POST":
            excel_file = request.FILES["excel_file"]
            if not excel_file.name.endswith('.xlsx'):
                self.message_user(request, "This is not an Excel file")
                return HttpResponseRedirect(request.path_info)

            df = pd.read_excel(excel_file, engine='openpyxl')

            now = timezone.now()
            year = now.year
            semester = '1' if now.month < 6 else '2'

            for _, row in df.iterrows():
                course_id = row['course_id']
                course_name = row['course_name']
                instructor = row['instructor']
                credits = row['credits']
                classification = row['classification']
                course_week = row['course_week'].strip('[]').replace("'", "").split(', ')
                course_period = row['course_period'].strip('[]').replace("'", "").split(', ')
                course_room = row['course_room'].strip('[]').replace("'", "").split(', ')

                Course.objects.create(
                    course_id=course_id,
                    course_name=course_name,
                    instructor=instructor,
                    credits=int(credits),
                    classification=classification,
                    year=year,
                    semester=semester,
                    course_week=course_week,
                    course_period=course_period,
                    course_room=course_room
                )
            self.message_user(request, "Excel file has been imported")
            return HttpResponseRedirect(reverse("admin:app_course_changelist"))

        form_html = '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="excel_file" accept=".xlsx">
            <button type="submit">Upload</button>
        </form>
        '''
        context = dict(
            self.admin_site.each_context(request),
            form_html=format_html(form_html)
        )
        return render(request, "admin/upload_excel.html", context)

admin.site.register(Course, CourseAdmin)
