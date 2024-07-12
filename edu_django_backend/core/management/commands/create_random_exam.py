# your_app/management/commands/create_random_exam.py

from django.core.management.base import BaseCommand
from core.models import RandomExam, Course

class Command(BaseCommand):
    help = 'Create a random exam'

    def add_arguments(self, parser):
        parser.add_argument('exam_type', type=str, help='The Type of the exam')
        parser.add_argument('--num_questions', type=int, default=10, help='Number of questions in the exam')

    def handle(self, *args, **options):
        num_questions = options['num_questions']
        exam_type = options['exam_type']
        random_exam = RandomExam.objects.create_random_exam(exam_type, num_questions)
        self.stdout.write(self.style.SUCCESS(f'Successfully created random exam with ID {random_exam.id}'))
        
        