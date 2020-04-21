import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstProject.settings')

import django

django.setup()



import random
from firstApp.models import AccRecord,Webpage,Topic
from faker import Faker

fakegen=Faker()
topics=['Search','Social','Market','News','Game']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entr in range(N):



        top=add_topic()

        fakeUrl=fakegen.url()
        fakeDate=fakegen.date()
        fakeName=fakegen.company()


        webpg=Webpage.objects.get_or_create(topic=top,url=fakeUrl,name=fakeName)[0]
        acc_rec=AccRecord.objects.get_or_create(name=webpg,date=fakeDate)[0]

if __name__=='__main__':
    print("populating script")
    populate(20)
    print("populating complete")
