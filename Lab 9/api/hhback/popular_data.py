
from django.core.management.base import BaseCommand
from hhback.models import Company, Vacancy

class Command(BaseCommand):
    help = 'Populate example data for Companies and Vacancies'

    def handle(self, *args, **options):
        company1 = Company.objects.create(
            name='TechCorp',
            description='A tech company specializing in software development.',
            city='Silicon Valley',
            address='123 Tech Street'
        )

        company2 = Company.objects.create(
            name='FashionHub',
            description='A fashion retail company with global presence.',
            city='New York',
            address='456 Fashion Avenue'
        )

        Vacancy.objects.create(
            name='Software Engineer',
            description='Join our talented team of developers!',
            salary=100000.0,
            company=company1
        )

        Vacancy.objects.create(
            name='Fashion Designer',
            description='Passionate about trends? Apply now!',
            salary=80000.0,
            company=company2
        )

        self.stdout.write(self.style.SUCCESS('Example data added successfully!'))
