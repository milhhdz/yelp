import json
import os

# from ..models import YelpUser
from yelp.models.business import Business
from yelp.models.users import YelpUser
from yelp.models.reviews import Review

# def run():
#     with open(f"{os.getcwd()}/data/user100k.json", "r") as reader:
#         while True:
#             line = reader.readline()
#             if not line:
#                 break
#             data = json.loads(line)
#             YelpUser.objects.create(**data)

# def run():
#     data_info = [
#         ("business10k.json", Business),
#         # ("user100k.json", YelpUser),
#         # ("review1M.json", Review),
#     ]

#     for file_name, class_model in data_info:
#         with open(f"/home/yelp/yelp/scripts/data/{file_name}", "r") as reader:
#             for idx, line in enumerate(reader):
#                 if not line:
#                     break
#                 data = json.loads(line)
#                 if "categories" in data and data["categories"] != None:
#                     print(idx)
#                     print(data["categories"])
#                     data["categories"] = data["categories"].split(",")

#                 if "friends" in data and data["friends"] != None:
#                     data["friends"] = data["friends"].split(",")

#                 if "elite" in data and data["elite"] != None:
#                     data["elite"] = data["elite"].split(",")




#                 class_model.objects.create(**data)



import time
from io import StringIO
import pandas as pd

from contextlib import closing

from django_bulk_load import bulk_insert_models

def in_memory_csv(data):
    """Creates an in-memory csv.

    Assumes `data` is a list of dicts
    with native python types."""

    mem_csv = StringIO()
    pd.DataFrame(data).to_csv(mem_csv, index=False)
    mem_csv.seek(0)
    return mem_csv

# def run():
#     data_info = [
#         # ("business10k.json", Business),
#         ("user100k.json", YelpUser),
#         # ("review1M.json", Review),
#     ]

#     for file_name, class_model in data_info:
#         with open(f"/home/yelp/yelp/scripts/data/{file_name}", "r") as reader:
#             list_users = []
#             for idx, line in enumerate(reader):
#                 if not line:
#                     break
#                 data = json.loads(line)

#                 list_users.append( YelpUser(**data) )
#             print("----")

#             inicio = 0
#             fin = 1000
#             while(fin <= 100000):
#                 new_list = list_users[inicio:fin]
#                 bulk_insert_models(new_list)
#                 time.sleep(2)
#                 print(f"----\n{fin}\n----")
#                 inicio = fin
#                 fin += 1000


def run():
    data_info = [
        # ("business10k.json", Business),
        # ("user100k.json", YelpUser),
        ("review1M.json", Review),
    ]

    for file_name, class_model in data_info:
        with open(f"/home/yelp/yelp/scripts/data/{file_name}", "r") as reader:
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
                time.sleep(2)
                print(f"----\n{fin}\n----")
                inicio = fin
                fin += 5000

                print(f"----\n{time.time() - time_inicio}\n----")
            

                