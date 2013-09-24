"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to {{ project_name }}/local_settings.py. It should not be checked into
your code repository.

"""

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Wil Linssen', 'wil@linssen.me'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'dev.db'),
    }
}

# ROOT_URLCONF = '{{ project_name }}.urls.local'
# WSGI_APPLICATION = '{{ project_name }}.wsgi.local.application'
