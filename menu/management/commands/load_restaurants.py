import csv
import os
import json
from django.core.management.base import BaseCommand
from menu.models import Restaurant

class Command(BaseCommand):
    help = 'Load restaurants from restaurants_small.csv'

    def handle(self, *args, **kwargs):
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        file_path = os.path.join(project_root, 'restaurants_small.csv')
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Create and save the Restaurant instance
                Restaurant.objects.create(
                    restaurant_id=row['id'],
                    name=row['name'],
                    location=row['location'],
                    items=json.loads(row['items']),
                    full_details=json.loads(row['full_details']) if row['full_details'] else None
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded restaurants data'))
