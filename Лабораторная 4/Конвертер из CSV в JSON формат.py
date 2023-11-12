# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    dict_list = list()
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as f:  # TODO считать содержимое csv файла
        data = csv.DictReader(f)
        for i in data:
            dict_list.append(i)
    # print(dict_list)
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        # TODO Сериализовать в файл с отступами равными 4
        json_f = json.dumps(dict_list, indent=4, ensure_ascii=False)
        f.write(json_f)
if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
