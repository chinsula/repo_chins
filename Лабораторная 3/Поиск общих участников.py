# TODO Напишите функцию find_common_participants
def find_common_participants(part_1group, part_2group, sep_=","):
    part_1group = part_1group.split(sep_)
    part_2group = part_2group.split(sep_)
    intersection_set = set(part_1group).intersection(part_2group)
    intersection_set = list(intersection_set)
    intersection_set.sort()
    return intersection_set
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))

