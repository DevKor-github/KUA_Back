# # coursetable/course_table/management/commands/import_multiple_csv.py

# import csv
# import os
# from django.core.management.base import BaseCommand
# from course_table.models import Course  # 앱의 모델에 맞게 수정해야 합니다

# class Command(BaseCommand):
#     help = 'Load multiple CSV files of courses'

#     def add_arguments(self, parser):
#         parser.add_argument('csv_files', nargs='+', type=str)

#     def handle(self, *args, **kwargs):
#         csv_files = kwargs['csv_files']
#         for csv_file in csv_files:
#             self.import_data(csv_file)

#     def import_data(self, csv_file):
#         with open(csv_file, newline='', encoding='utf-8') as file:
#             reader = csv.reader(file)
#             next(reader)  # Skip the header row
#             for row in reader:
#                 Course.objects.create(
#                     # year?
#                     # year = ..
#                     #학수번호
#                     course_id=row[0],
#                     #강의명
#                     course_name=row[1],
#                     #교수명
#                     instructor=row[2],
#                     #학점
#                     credits=int(row[3]),  # Assuming credits is an integer field
#                     #이수구분
#                     classification=row[4],
#                     #요일
#                     course_week=row[5],
#                     #교시
#                     course_period=row[6],
#                     #장소
#                     course_room=row[7],
#                 )
#         self.stdout.write(self.style.SUCCESS(f'Data from {os.path.basename(csv_file)} imported successfully'))


import os
import openpyxl
from django.core.management.base import BaseCommand
from course_table.models import Course  # 앱의 모델에 맞게 수정해야 합니다

class Command(BaseCommand):
    help = 'Load multiple Excel files of courses'

    def add_arguments(self, parser):
        parser.add_argument('excel_files', nargs='+', type=str)

    def handle(self, *args, **kwargs):
        excel_files = kwargs['excel_files']
        for excel_file in excel_files:
            self.import_data(excel_file)

    def import_data(self, excel_file):
        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            Course.objects.create(
                course_id=row[0],
                course_name=row[1],
                instructor=row[2],
                credits=int(row[3]),  # Assuming credits is an integer field
                classification=row[4],
                course_week=row[5],
                course_period=row[6],
                course_room=row[7],
            )
        self.stdout.write(self.style.SUCCESS(f'Data from {os.path.basename(excel_file)} imported successfully'))
