from django_orm.utils.version import get_version
import os
import django_orm


VERSION = (4, 1, 2, "final", 0)

__version__ = get_version(VERSION)


def setup(set_prefix=True):
    """
    Configure the settings (this happens as a side effect of accessing the
    first setting), configure logging and populate the app registry.
    Set the thread-local urlresolvers script prefix if `set_prefix` is True.
    """
    from django_orm.apps import apps
    from django_orm.conf import settings

    apps.populate(settings.INSTALLED_APPS)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django_orm.setup()
