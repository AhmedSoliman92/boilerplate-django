import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "rename a django project name."

    def add_arguments(self, parser):
        parser.add_argument("new_project_name", type=str, help="The new project name")

    def handle(self, *args, **options):
        new_project_name = options["new_project_name"]

        files_to_rename = [
            "boilerplate_project/settings/base.py",
            "boilerplate_project/wsgi.py",
            "manage.py",
        ]
        folder_to_rename = "boilerplate_project"

        for file_to_rename in files_to_rename:
            with open(file_to_rename, "r") as file:
                data = file.read()
            data = data.replace("boilerplate_project", new_project_name)

            with open(file_to_rename, "w") as file:
                file.write(data)

        os.rename(folder_to_rename, new_project_name)
        self.stdout.write(
            self.style.SUCCESS("project has been renamed to %s" % new_project_name)
        )
