import json
import os

# from ..models import YelpUser

# def run():
#     with open(f"{os.getcwd()}/data/user100k.json", "r") as reader:
#         while True:
#             line = reader.readline()
#             if not line:
#                 break
#             data = json.loads(line)
#             YelpUser.objects.create(**data)

def run():
    data_info = [
        ("business10k.json", "Clase_Negocio"),
        ("user100k.json", "Clase_Usuario"),
        ("review1M.json", "Clase_Reseña"),
    ]

    for file_name, class_model in data_info:
        with open(f"/home/yelp/utils/data/{file_name}", "r") as reader:
            print(class_model, "\n\n\n")
        # for line in reader:
        #     if not line:
        #         break
        #     data = json.loads(line)
            
        
# def insert_business_data():
#     with open(f"{os.getcwd()}/data/business10k.json", "r") as reader:
#     for line in reader:
#         if not line:
#             break
#         data = json.loads(line)

run()