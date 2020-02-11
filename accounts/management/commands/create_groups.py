from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):

    help = "Create groups for user"

    def handle(self, *args, **options):
        group_list = ('Admin', 'Editor', 'Custom_user')
        for group in group_list:
            name,created = Group.objects.get_or_create(name=group)

