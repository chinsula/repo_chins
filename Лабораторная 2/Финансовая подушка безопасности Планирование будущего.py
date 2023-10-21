money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

count = 0
total_rem = money_capital + salary - spend
spend_dep = spend
while total_rem >= 0:
    inc_cost = spend_dep * increase
    spend_dep += inc_cost
    total_rem = (total_rem + salary) - spend_dep
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
