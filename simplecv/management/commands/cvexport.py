import os
from django.core.management.base import BaseCommand, CommandError
from simplecv.utils import load_cv
from simplecv.export import export


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument('cv_filename')
        parser.add_argument('output_type', choices=['html', 'docx', 'pdf', 'txt', 'all'])
        parser.add_argument(
            '-y',
            action='store_true',
            dest='yes',
            default=False,
            help='Indicate YES to all prompts',
        )
 
    def handle(self, *args, **options):
        if options['output_type'] == 'all':
            output_types = export.all_exports_types
        else:
            output_types = [options['output_type']]

        dirname, cv_filename = os.path.split(options['cv_filename'])
        base, ext = os.path.splitext(cv_filename)

        cv = load_cv(options['cv_filename'])
        for kind in output_types:
            output_filename = os.path.join(dirname, '{}.{}'.format(base, kind))
            with open(output_filename, 'wb') as fp:
                export(fp, cv, kind)

        self.stdout.write(self.style.SUCCESS('Success'))
