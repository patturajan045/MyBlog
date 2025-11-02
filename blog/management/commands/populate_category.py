from typing import Any
from django.core.management.base import BaseCommand
from blog.models import Category



class Command(BaseCommand):
    help = "This command populates and inserts Post data into the database"

    def handle(self, *args: Any, **options: Any):

        # Delete Exixting Data
        Category.objects.all().delete()

        categories = ['sports','Technology','Science','Art','Food']

        for category_name in categories:
            Category.objects.create(name = category_name)
 
        self.stdout.write(self.style.SUCCESS("Completed inserting post data successfully!"))
