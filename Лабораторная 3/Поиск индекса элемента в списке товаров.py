# TODO Напишите функцию для поиска индекса товара
def func(list_item, name_item):
    for i in range(len(list_item)):
        if list_item[i] == name_item:
            index_item = i
            return index_item

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
func(items_list, "банан")

for find_item in ['банан', 'груша', 'персик']:
    index_item = func(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
