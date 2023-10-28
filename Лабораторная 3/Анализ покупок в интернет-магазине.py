# TODO Напишите функцию find_common_items
from typing import Set, Any


def find_common_items(last_week_purchases, current_week_purchases):
    intersection_set = set(last_week_purchases).intersection(current_week_purchases)
    intersection_set = list(intersection_set)
    intersection_set.sort()
    return intersection_set

last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']
# print(find_common_items(last_week_items, current_week_items))
# find_common_items(last_week_items, current_week_items)
print(f"Общие товары: {find_common_items(last_week_items, current_week_items)}")  # TODO Распечатайте общие товары
