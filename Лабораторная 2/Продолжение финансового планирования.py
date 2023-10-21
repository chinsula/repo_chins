salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов


count = 0
cons_month = salary - spend
spend_dep = spend
for i in range(1, 10):
    inc_cost = spend_dep * increase
    spend_dep += inc_cost
    cons_month += (salary - spend_dep)

print(f"Подушка безопасности, чтобы протянуть {i + 1} месяцев без долгов:", round(cons_month, 2) * -1)
