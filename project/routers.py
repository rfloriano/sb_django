# from django.db import models
# from django.conf import settings
# from django.db.models import sql
# from django.db.transaction import savepoint_state

# try:
#     import thread
# except ImportError:
#     import dummy_thread as thread


# class MultiDBManager(models.Manager):
#     def __init__(self, database, *args, **kwargs):
#         self.database = database
#         super(MultiDBManager, self).__init__(*args, **kwargs)

#     def get_query_set(self):
#         qs = super(MultiDBManager, self).get_query_set()
#         qs.query.connection = self.get_db_wrapper()
#         return qs

#     def get_db_wrapper(self):
#         database = settings.DATABASES[self.database]
#         backend = __import__('django.db.backends.' + database['DATABASE_ENGINE']
#             + ".base", {}, {}, ['base'])
#         backup = {}
#         for key, value in database.iteritems():
#             backup[key] = getattr(settings, key)
#             setattr(settings, key, value)
#         wrapper = backend.DatabaseWrapper()
#         wrapper._cursor(settings)
#         for key, value in backup.iteritems():
#             setattr(settings, key, value)
#         return wrapper

#     def _insert(self, values, return_id=False, raw_values=False):
#         query = sql.InsertQuery(self.model, self.get_db_wrapper())
#         query.insert_values(values, raw_values)
#         ret = query.execute_sql(return_id)
#         query.connection._commit()
#         thread_ident = thread.get_ident()
#         if thread_ident in savepoint_state:
#             del savepoint_state[thread_ident]
#         return ret

class Router(object):
    """A router to control all database operations on models in
    the myapp application"""

    def db_for_read(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        if model._meta.app_label == 'old' or model._meta.app_label == 'migration':
            return 'old'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        # if model._meta.app_label == 'myapp':
        #     return 'other'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in myapp is involved"
        if obj1._meta.app_label == 'myapp' or obj2._meta.app_label == 'myapp':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the myapp app only appears on the 'other' db"
        # if db == 'other':
        #     return model._meta.app_label == 'myapp'
        # elif model._meta.app_label == 'myapp':
        #     return False
        # return None
        if model._meta.app_label == 'migration':
            return False
        return True
