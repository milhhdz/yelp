import json
import time
from django_bulk_load import bulk_insert_models


from yelp.models.business import Business
from yelp.models.users import YelpUser
from yelp.models.reviews import Review

def insert_data_business():
    with open("/home/yelp/yelp/scripts/data/business10k.json", "r") as reader:
        list_business = []
        for idx, line in enumerate(reader):
            if not line:
                break
            data = json.loads(line)
            if "categories" in data and data["categories"] != None:
                print(idx)
                print(data["categories"])
                data["categories"] = data["categories"].split(",")

            if "friends" in data and data["friends"] != None:
                data["friends"] = data["friends"].split(",")

            if "elite" in data and data["elite"] != None:
                data["elite"] = data["elite"].split(",")


            list_business.append( Business(**data) )
        
        inicio = 0
        fin = 5000
        while(fin <= 10000):
            time_inicio = time.time()

            new_list = list_business[inicio:fin]
            bulk_insert_models(new_list)
            print(f"----\n{fin}\n----")
            inicio = fin
            fin += 5000
            time.sleep(2)

            print(f"----\n{time.time() - time_inicio}\n----")

def insert_data_users():    
    with open("/home/yelp/yelp/scripts/data/user100k.json", "r") as reader:
        list_users = []
        for idx, line in enumerate(reader):
            if not line:
                break
            data = json.loads(line)

            list_users.append( YelpUser(**data) )

        inicio = 0
        fin = 5000
        while(fin <= 100000):
            time_inicio = time.time()

            new_list = list_users[inicio:fin]
            bulk_insert_models(new_list)
            print(f"----\n{fin}\n----")
            inicio = fin
            fin += 5000
            print(f"----\n{time.time() - time_inicio}\n----")
            time.sleep(2)

def insert_data_reviews():
    with open("/home/yelp/yelp/scripts/data/review1M.json", "r") as reader:
        list_users = []
        for idx, line in enumerate(reader):
            if idx == 100000:
                break
            data = json.loads(line)

            try:
                user = YelpUser.objects.only("user_id").get(user_id=data["user_id"])
                data["user_id"] = user
            except YelpUser.DoesNotExist:
                data["user_id"] = None
            try:
                business = Business.objects.only("business_id").get(business_id=data["business_id"])
                data["business_id"] = business
            except Business.DoesNotExist:
                data["business_id"] = None

            list_users.append( Review(**data) )

        inicio = 0
        fin = 5000
        while(fin <= 100000):
            time_inicio = time.time()

            new_list = list_users[inicio:fin]
            bulk_insert_models(new_list)
            print(f"----\n{fin}\n----")
            inicio = fin
            fin += 5000
            time.sleep(2)

            print(f"----\n{time.time() - time_inicio}\n----")


def run():
    print("---BUSINESS---")
    insert_data_business()
    print("---USERS---")
    insert_data_users()
    print("---REVIEWS---")
    insert_data_reviews()