from datetime import date
from operator import imod
import os
from unicodedata import name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Second_project.settings')

import django
django.setup()


##FAKE POP SCRIPT

import random
from Second_App.models import Accessrecord,Webpage, topic
from faker import Faker

fakegen=Faker()
topic =['Search', 'Social', 'Marketplace', 'News', 'Games']


# def add_topic():
#     # t=topic.objects.get_or_create(top_name=random.choice(topic))[0]
#     t.save()
#     return t

def add_topic():
    to = topic.objects.get_or_create(top_name=random.choice(topic))[0]
    to.save()
    return to


def populate(N=5):
    for entry in range(N):

        #add the topic for the country
        top=add_topic()


        #create the fake data for entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        # create the new webpage entry
        webpg=Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]


        # create a fake access record for that webpage

        acc_rec=Accessrecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("populating Script!")
    populate(20)
    print("Populating Complete!")
