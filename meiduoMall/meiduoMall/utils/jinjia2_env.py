from django.contrib.staticfiles.storage import staticfiles_storage

from jinja2 import Environment

from django.urls import reverse


def jinjia2_enviroment(**options):

    env = Environment(**options)

    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })

    return env



"""
确保可以使用模板引擎中的 {{url('')}} {{static('')}}这类语句
"""