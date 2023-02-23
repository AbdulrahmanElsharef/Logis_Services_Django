import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django 
django.setup()

from faker import Faker
import random
from service.models import *


def seed_service(n):
    fake = Faker()
    images = ['features-1.jpg','features-2.jpg','features-3.jpg','features-4.jpg','logistics-service_1.jpg','packaging-service.jpg','service-details.jpg','trucking-service.jpg',]
    for x in range(n):
        Service.objects.create(
            name = fake.name() ,
            title=fake.text(max_nb_chars=50) ,
            subtitle=fake.text(max_nb_chars=200) ,
            description=fake.text(max_nb_chars=1000) ,
            ser_image = f"service/{images[random.randint(0,7)]}",
            det_image = f"service/{images[random.randint(0,7)]}",
        )
    print(f'{n} Service Seeded')

def seed_Condition(n):
    fake=Faker()
    for x in range(n):
       Condition.objects.create(
          conditione=fake.text(max_nb_chars=150),
          service=Service.objects.get(id=random.randint(1,49))
        )
    print(f'{n} Condition Seeded')
       
def seed_LastService(n):
    fake=Faker()
    images = ['features-1.jpg','features-2.jpg','features-3.jpg','features-4.jpg','logistics-service_1.jpg','packaging-service.jpg','service-details.jpg','trucking-service.jpg',]

    for x in range(n):
       LastService.objects.create(
            service=Service.objects.get(id=random.randint(1,49)),
            title=fake.text(max_nb_chars=50) ,
            subtitle=fake.text(max_nb_chars=200) ,
            description=fake.text(max_nb_chars=1000) ,
            image = f"service/{images[random.randint(0,7)]}",
        )
    print(f'{n} LastService Seeded')

def seed_team(n):
    fake=Faker()
    images = ['team-1.jpg','team-2.jpg','team-3.jpg']
    for x in range(n):
       OurTeam.objects.create(
            name = fake.name() ,
            job=fake.text(max_nb_chars=50) ,
            job_info=fake.text(max_nb_chars=200) ,
            image = f"OurTeam/{images[random.randint(0,2)]}",
        )
    print(f'{n} team Seeded')
    
    
def seed_Review(n):
    fake=Faker()
    for x in range(n):
       Review.objects.create(
            service=Service.objects.get(id=random.randint(1,49)),
            rate=random.randint(1,5) ,
            review=fake.text(max_nb_chars=500) ,
        )
    print(f'{n} Review Seeded')
    
def seed_FaqAsked(n):
    fake=Faker()
    for x in range(n):
        FaqAsked.objects.create(
        ask=fake.text(max_nb_chars=50),
        answer=fake.text(max_nb_chars=300),        )
    print(f'{n} FaqAsked Seeded')



seed_FaqAsked(15)
# seed_service(25)
# seed_Condition(50)
# seed_LastService(25)
# seed_team(20)
# seed_Review(50)
# def seed_product(n):
#     fake = Faker()
#     images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
#     flags = ['New','Feature','Sale']

#     for x in range(n):
#         Product.objects.create(
#             name = fake.name() , 
#             image = f"products/{images[random.randint(0,12)]}" , 
#             price = round(random.uniform(20.99,99.99),2) , 
#             sku = random.randint(1000,1000000) , 
#             subtitle = fake.text(max_nb_chars=300) , 
#             description = fake.text(max_nb_chars=5000) , 
#             flag = flags[random.randint(0,2)] , 
#             brand = Brand.objects.get(id=random.randint(1,120)),  
#         )
#     print(f'{n} Products Seeded')


# def seed_product_images(n):
#     fake = Faker()
#     images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
#     for x in range(n): 
#         ProductImages.objects.create(
#             product = Product.objects.get(id=random.randint(1,5000)) , 
#             image = f"productimages/{images[random.randint(0,12)]}" , 
#         )
#     print(f'{n} Products Images Seeded')

# # seed_brand(100)
# # seed_product(5000)
# seed_product_images(10000)