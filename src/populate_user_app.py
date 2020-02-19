import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

import random
from user.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):

    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        fake_user = User.objects.get_or_create(First_name=fake_first_name, Last_name=fake_last_name, Email=fake_email)


if __name__ == '__main__':
    populate()

