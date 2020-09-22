import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myfirstdjango.settings')

import django
django.setup()

## FAKE POP SCRIPT

import random

from Firstapp.models import Accessrecord,Topic,webpage,user
from faker import Faker

fakegen = Faker()

topics = ["search","social",'Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_first = fakegen.name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.email()
        webpg = webpage.objects.get_or_create(topic = top,url = fake_url,name = fake_name)[0]
        accrec = Accessrecord.objects.get_or_create(name = webpg,date = fake_date)[0]
        user_details = user.objects.get_or_create(first_name = fake_first,
                                                  last_name = fake_last,email = fake_email)

if __name__=='__main__':
    print('pupulating script')
    populate(20)
    print('populating complete')
