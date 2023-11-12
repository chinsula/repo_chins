# TODO решите задачу

import json

def task() -> float:
    FILE_NAME = "input.json"
    sum_prod_dict = 0
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data:
            sum_prod_dict += i["score"] * i["weight"]
        return round(sum_prod_dict, 3)


print(task())
