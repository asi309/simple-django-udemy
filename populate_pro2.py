import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')

import django
django.setup()

from pro2.models import User
import random
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        email = fakegen.email()
        fname = fakegen.first_name()
        lname = fakegen.last_name()

        user = User.objects.get_or_create(fname=fname, lname=lname, email=email)[0]


if __name__ == '__main__':
    print('Populating User Details')
    populate(20)
    print("Populated List with user details")