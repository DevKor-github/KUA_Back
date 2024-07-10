import os
import openpyxl
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from course_table.models import Course

class Command(BaseCommand):
    help = 'Load multiple Excel files of courses'

    def add_arguments(self, parser):
        parser.add_argument('excel_files', nargs='+', type=str)

    def handle(self, *args, **kwargs):
        excel_files = kwargs['excel_files']
        for excel_file in excel_files:
            try:
                self.import_data(excel_file)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed to import data from {os.path.basename(excel_file)}: {str(e)}'))

    def import_data(self, excel_file):
        try:
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.active
            for row in sheet.iter_rows(min_row=2, values_only=True):
                try:
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
                except IntegrityError:
                    self.stdout.write(self.style.WARNING(f'Course {row[0]} already exists. Skipping...'))
        
            self.stdout.write(self.style.SUCCESS(f'Data from {os.path.basename(excel_file)} imported successfully'))
        except FileNotFoundError:
            raise CommandError(f'File not found: {excel_file}')
        except Exception as e:
            raise CommandError(f'Failed to import data from {excel_file}: {str(e)}')
