import os
#configuring  settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'leve1_project.settings')

import django
#this will setup and configure project settings
django.setup()

#FAKE POPULATION SCRIPT
import random
from leve1_app.models import AccessRecord,Webpage,topic
from faker import Faker

# fakegen = Faker()
#
#
# topics = ['search','social','marketplace','games']
#
# def add_topic():
#     t = topic.objects.get_or_create(topic_name = random.choice(topics))[0]
#     t.save()
#     return t
#
# def populate(N=5):
#     for entry in range(N):
#         #get the topic for entry
#         top = add_topic()
#
#         #create fake data for that entry
#         fake_url = fakegen.url()
#         fake_date = fakegen.date()
#         fake_name = fakegen.company()
#
#         #create new webpage entry
#         webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
#
#         #create a fake access record for that webpg
#
#         acc_rcrd = AccessRecord.objects.get_or_create(name=fake_name,date=fake_date)[0]
#
#
# if __name__ == "__main__":
#     print("population in progress")
#     populate(10)
#     print("Done")
#
#
# import os
# # Configure settings for project
# # Need to run this before calling models from application!
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
#
# import django
# # Import settings
# django.setup()
#
# import random
# from first_app.models import Topic,Webpage,AccessRecord
# from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t



def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry
        top = add_topic()

        # Create Fake Data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create new Webpage Entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')

#
#
