import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstProject.settings')

import django
django.setup()

# FAKE POPULATION SCRIPT
import random
from firstApp.models import Topic, Webpage, AccessRecord
from faker import Faker
from users.models import MyUsers

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0] # [0] returns reference to
    t.save()                                                             # model instance
    return t

def populate(N=5):
    for entry in range(N):
        # Get the topic for the entry
        top = add_topic()

        # Create fake data for that entry
        fakeurl = fakegen.url()
        fakedate = fakegen.date()
        fakename = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fakeurl, name=fakename)[0]

        # Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fakedate)[0]



def userDataPopulate(N):
    for item in range(N):
        fakeFname = fakegen.name()
        fakeLname = fakegen.name()
        fakeEmail = fakegen.email()

        t = MyUsers.objects.get_or_create(fname=fakeFname, lname=fakeLname, myEmail=fakeEmail)[0]
        t.save()



if __name__ == '__main__':
    print('Populating script!')
    #populate(20)
    userDataPopulate(10)
    print('Populating complete!')
