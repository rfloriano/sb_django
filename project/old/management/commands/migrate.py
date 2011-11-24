from django.core.management.base import BaseCommand, CommandError
from old.models import *
from migration.models import *

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        if args:
            modules = args
        else:
            modules = dir(__import__("old.models").models)[:-6] + dir(__import__("migration.models").models)[:-6]

        for mod in modules:
            # try:
                self.verbose("Migrating %s ...\n" % mod)
                queryset = eval("%s.objects.all()" % mod)
                for obj in queryset:
                    obj.save()
                self.verbose('Successfully migrated database "%s"\n' % mod)
            # except Exception, e:
            #     self.verbose('Exception in table %s ----> "%s"\n' % (mod, e))

    def verbose(self, msg):
        self.stdout.write(msg)
