#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#ここから自分で 9行目シングルクオーテーション
"""
def main(): 
    """'Run administrative tasks.'"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
"""
#ここまで

if __name__ == '__main__':
    # If WEBSITE_HOSTNAME is defined as an environment variable, then we're running
    # on Azure App Service and should use the production settings.
    settings_module = "myapp.production" if 'WEBSITE_HOSTNAME' in os.environ else 'myapp.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)