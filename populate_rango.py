import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views': 10},
        {'title': 'How to Think like a computer scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views' : 20},
        {'title': 'Learn Python in 10 minutes',
         'url': 'http://www.korokithakis.net/tutorials/python',
         'views': 30}]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'http://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 5},
        {'title': 'Django rocks',
         'url': 'http://www.djangorokcs.com/',
         'views': 15},
        {'title': 'How to Tango with Django',
         'url': 'http://www.Tangowithdjango.com/',
         'views': 25}]

    other_pages = [
            {'title': 'Bottle',
             'url':'http://bottlepy.org/docs/dev/',
             'views': 13},
            {'title': 'Flask',
             'url': 'http://flask.pocoo.org',
             'views': 17}]

    pascal_pages = []
    perl_pages = []
    php_pages = []
    prolog_pages = []
    postscript_pages = []
    programming_pages = []

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16},
            'Pascal': {'pages': pascal_pages, 'views': 100, 'likes': 3},
            'Perl': {'pages': perl_pages, 'views': 99, 'likes': 16},
            'Php': {'pages': php_pages, 'views': 75, 'likes': 12},
            'Prolog': {'pages': prolog_pages, 'views': 40, 'likes': 30},
            'PostScript': {'pages': postscript_pages, 'views': 116, 'likes': 26},
            'Programming': {'pages': programming_pages, 'views': 43, 'likes': 12},}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print('- {0} - {1}'.format(str(c), str(p)))

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.name=name
    c.views=views
    c.likes=likes
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()