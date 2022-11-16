# This is a standalone Django ORM

## Quick setup
Create a virtual environment <br>
**`python3 -m venv venv`<br>
`source venv/bin/activate`**

Clone the repo, move **django_orm** folder to your root folder or venv<br>

Install the requirements <br>
**`pip install -r requirements.txt`**
Keep **example/** and **settings.py** on your root folder

**example** acts like app in Django, you could change the name to anything according to django app naming rules, make sure to replace the app name in **INSTALLED_APPS** in **settings.py**

Create your models exactly as you do with django 
copy your models to **example/**
configure **settings.py** exactly as you do with django
<br><br>
This ORM is extracted from **Django 4.1** so new orm features like async queries are supported
<br>
Here is an example of how you can use django_orm from your code,

**main.py**
```
import asyncio

import django_orm
from example.models import Person

from django_orm.utils import timezone


def sync_example():
      Person.objects.create(name='xyz', joined_date=timezone.now())

      for p in Person.objects.all():
            print(f'name: {p.name} date: {p.joined_date}')

async def async_example():
      await Person.objects.acreate(name='xyz', joined_date=timezone.now())

      async for p in Person.objects.all():
            print(f'name: {p.name} date: {p.joined_date}')


if __name__ == "__main__":
      sync_example()
      asyncio.run(async_example())
```
<br>

**Make sure to keep the name of settings.py and always import django_orm at the top of the file<br>
`import django_orm`<br>
Make sure to use "django_orm" instead of "django" during imports, for example `from django_orm.db import models` should be used to import db.models.**
<br><br>
Most of the feature that an independent orm doesnt necessarily require is removed so keep that in mind while using this project. So no formfields, no development web server.
You should be able to directly refer [django documentation](https://docs.djangoproject.com/en/4.1/) to refer and clear any doubts related to django-orm.
View this orm as django-orm without whole django library not as a separate orm.
