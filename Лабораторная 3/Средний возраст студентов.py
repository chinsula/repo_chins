# TODO Напишите функцию calculate_average_age для расчета среднего возраста студентов
def calculate_average_age(total_students):
    total_heigt = []
    for heght in total_students.values():
        total_heigt.append(heght)
    average_value = sum(total_heigt) / len(total_heigt)
    return average_value
students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}

print(f"Средний возраст студентов: {calculate_average_age(students_dict)}")  # TODO Распечатайте средний возраст студентов
