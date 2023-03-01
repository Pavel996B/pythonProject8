num_tickets = int(input("Сколько билетов вы хотите приобрести? "))
total_cost = 0

for i in range(num_tickets):
    age = int(input("Какой возраст посетителя #" + str(i+1) + "? "))
    if age < 18:
        ticket_cost = 0
    elif age < 25:
        ticket_cost = 990
    else:
        ticket_cost = 1390
    total_cost += ticket_cost

if num_tickets > 3:
    total_cost *= 0.9

print("Общая стоимость билетов составляет: " + str(total_cost) + " руб.")