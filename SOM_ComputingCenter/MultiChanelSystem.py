import random
import numpy as np


class Event:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def show(self):
        print(self.name, '--', self.time)


f = int(input("Выберите функцию: \n 1. Ввести с клавиатуры; \n 2. Запустить стандартные значения. \n"))

if f == 1:
    print('Введите последовательно следующую информацию:')
    print()
    tasks = int(input('Количество заданий: '))
    # стандартное значение = 200

    weight_1, weight_2, weight_3 = map(float, input('Веса распределения на три ЭВМ, через пробел: ').split())
    # стандартные значения = 0.4 0.3 0.3

    weight_evm_1_to_2, weight_evm_1_to_3 = map(float,
                                               input(
                                                   'Веса распределения из ЭВМ_1 в ЭВМ_2 и ЭВМ_3, через пробел: ').split())
    # стандартные значения = 0.3 0.7

    a1, b1 = map(int, input('Интервалы для ЭВМ_1, через пробел: ').split())
    # стандартные значения = 3 5

    a2, b2 = map(int, input('Интервалы для ЭВМ_2, через пробел: ').split())
    # стандартные значения = 2 4

    a3, b3 = map(int, input('Интервалы для ЭВМ_3, через пробел: ').split())
    # стандартные значения = 3 7
elif f == 2:

    # количество заданий
    tasks = 200

    # вероятность поступления заданий
    weight_1 = 0.4
    weight_2 = 0.3
    weight_3 = 0.3

    # вероятность перехода заданий на другую эвм
    weight_evm_1_to_2 = 0.3
    weight_evm_1_to_3 = 0.7

    # интервалы времени
    a1 = 3
    a2 = 3
    a3 = 5

    b1 = 5
    b2 = 4
    b3 = 7
else:
    print("Ошибка! Некорректно введены данные.")

events = []
now_time = 0 # текущее время



# глобальные переменные для ЭВМ 1
evm_1_total_tasks = 0 # общее время выполнения заданий
evm_1_total_time = 0  # общее время работы
evm_1_last = 0 # время обработки последней заявки
evm_1_relax = 0 # время простоя
evm_1_total_relax = 0 # общее время простоя ЭВМ
evm_1_total_queue = 0 # общее время простоя ЭВМ в очереди
evm_1_total = 0

# глобальные переменные для ЭВМ 2
evm_2_total_tasks = 0 # общее время выполнения заданий
evm_2_total_time = 0 # общее время работы
evm_2_last = 0 # время обработки последней заявки
evm_2_relax = 0 # время простоя
evm_2_total_relax = 0 # общее время простоя ЭВМ
evm_2_total = 0
evm_2_total_queue = 0 # общее время простоя ЭВМ в очереди
flag_2 = 0

# глобальные переменные для ЭВМ 3
evm_3_total_tasks = 0 # общее время выполнения заданий
evm_3_total_time = 0 # общее время работы
evm_3_last = 0 # время обработки последней заявки
evm_3_relax = 0 # время простоя
evm_3_total_relax = 0 # общее время простоя ЭВМ
evm_3_total = 0
evm_3_total_queue = 0 # общее время простоя ЭВМ в очереди
flag_3 = 0

evm_1_w = 0
evm_2_w = 0
evm_3_w = 0

def evm_1(task_number):
    global now_time, evm_1_relax, evm_1_last, evm_1_total_time, evm_1_total_relax, evm_1_total_tasks, evm_1_total_queue

    # количество заявок
    evm_1_total_tasks += 1

    # время простоя
    evm_1_relax = now_time - evm_1_last
    if evm_1_relax < 0:
        evm_1_relax = 0

    # если нужно время ожидания между заявками, то выводим каждый раз evm_1_relax
    #print('Интервалы между заявками для ЭВМ1:',round(evm_1_relax,2))

    # общее время простоя
    evm_1_total_relax += evm_1_relax

    # поступление заявки
    task_start = Event('ЭВМ 1 поступила заявка {}'.format(task_number), now_time)
    start_queue = now_time

    # время выполнения заявки
    evm_1_work = np.random.uniform(a1, b1)
    global evm_1_w
    evm_1_w = evm_1_work

    # время конца работы
    # если заявка есть
    if evm_1_last > now_time:
        evm_1_last = evm_1_last + evm_1_work
    # если заявки нет
    else:
        evm_1_last = now_time + evm_1_work

    # выполнение заявки
    task_end = Event('ЭВМ 1 выполнена заявка {}'.format(task_number), evm_1_last)
    end_queue = evm_1_last
    evm_1_total_queue += end_queue - start_queue

    # общее время работы = время всего простоя + время всей работы
    evm_1_total_time = evm_1_total_time + evm_1_relax + evm_1_work

    # заносим события в список
    events.append(task_start)
    events.append(task_end)

    # передаем задачу другой ЭВМ
    next_evm_number = random.choices((2, 3), weights=[weight_evm_1_to_2, weight_evm_1_to_3])

    # ЭВМ 2
    if next_evm_number == [2]:
        evm_2(i, 1, evm_1_last)

    # ЭВМ 3
    elif next_evm_number == [3]:
        evm_3(i, 1, evm_1_last)


def evm_2(task_number, enemy_task, enemy_time):
    global now_time, evm_2_relax, evm_2_last, evm_2_total_time, evm_2_total_relax, evm_2_total_tasks, evm_2_total_queue

    # кол-во заявок
    evm_2_total_tasks += 1

    # поступила задача от ЭВМ 1
    if enemy_task == 1:
        now_time = enemy_time

    # время простоя
    evm_2_relax = now_time - evm_2_last
    if evm_2_relax < 0:
        evm_2_relax = 0

    # если нужно время ожидания между заявками, то выводим каждый раз evm_2_relax
    #print('Интервалы между заявками для ЭВМ1:',round(evm_2_relax,2))

    # общее время простоя
    evm_2_total_relax += evm_2_relax

    # поступление заявки
    if enemy_task == 0:
        task_start = Event('ЭВМ 2 поступила заявка {}'.format(task_number), now_time)
    else:
        task_start = Event('ЭВМ 2 передана заявка {} от ЭВМ 1'.format(task_number), now_time)
    start_queue = now_time

    # время выполнения заявки
    evm_2_work = np.random.uniform(a2, b2)
    # evm_2_work = 10
    global evm_2_w
    evm_2_w = evm_2_work

    # время конца работы
    # если заявка есть
    if evm_2_last > now_time:
        evm_2_last = evm_2_last + evm_2_work
    # если заявки нет
    else:
        evm_2_last = now_time + evm_2_work

    # выполнение заявки
    if enemy_task == 0:
        task_end = Event('ЭВМ 2 выполнена заявка {}'.format(task_number), evm_2_last)
    else:
        task_end = Event('ЭВМ 2 выполнена переданная заявка {} от ЭВМ 1'.format(task_number), evm_2_last)
    end_queue = evm_2_last
    evm_2_total_queue += end_queue - start_queue

    # общее время работы = время всего простоя + время всей работы
    evm_2_total_time = evm_2_total_time + evm_2_relax + evm_2_work

    # заносим события в список
    events.append(task_start)
    events.append(task_end)


def evm_3(task_number, enemy_task, enemy_time):
    global now_time, evm_3_relax, evm_3_last, evm_3_total_time, evm_3_total_relax, evm_3_total_tasks, evm_3_total_queue

    # кол-во заявок
    evm_3_total_tasks += 1

    # поступила задача от ЭВМ 1
    if enemy_task == 1:
        now_time = enemy_time

    # время простоя
    evm_3_relax = now_time - evm_3_last
    if evm_3_relax < 0:
        evm_3_relax = 0

    # если нужно время ожидания между заявками, то выводим каждый раз evm_3_relax
    #print('Интервалы между заявками для ЭВМ1:',round(evm_3_relax,2))

    # общее время простоя
    evm_3_total_relax += evm_3_relax

    # поступление заявки
    if enemy_task == 0:
        task_start = Event('ЭВМ 3 поступила заявка {}'.format(task_number), now_time)
    else:
        task_start = Event('ЭВМ 3 передана заявка {} от ЭВМ 1'.format(task_number), now_time)
    start_queue = now_time

    # время выполнения заявки
    evm_3_work = np.random.uniform(a3, b3)
    # evm_3_work = 10
    global evm_3_w
    evm_3_w = evm_3_work

    # время конца работы
    # если заявка есть
    if evm_3_last > now_time:
        evm_3_last = evm_3_last + evm_3_work
    # если заявки нет
    else:
        evm_3_last = now_time + evm_3_work

    # выполнение заявки
    if enemy_task == 0:
        task_end = Event('ЭВМ 3 выполнена заявка {}'.format(task_number), evm_3_last)
    else:
        task_end = Event('ЭВМ 3 выполнена переданная заявка {} от ЭВМ 1'.format(task_number), evm_3_last)
    end_queue = evm_3_last
    evm_3_total_queue += end_queue - start_queue

    # общее время работы = время всего простоя + время всей работы
    evm_3_total_time = evm_3_total_time + evm_3_relax + evm_3_work

    # заносим события в список
    events.append(task_start)
    events.append(task_end)


for i in range(1, tasks + 1):
    task_interval = np.random.uniform(2, 4)
    global interval
    interval = task_interval
    evm_number = random.choices((1, 2, 3), weights=[weight_1, weight_2, weight_3])
    # добавляем время выдачи задачи
    now_time += task_interval

    # ЭВМ 1
    if evm_number == [1]:
        evm_1(i)

    # ЭВМ 2
    elif evm_number == [2]:
        evm_2(i, 0, 'str')

    # ЭВМ 3
    elif evm_number == [3]:
        evm_3(i, 0, 'str')


events_sorted = sorted(events, key=lambda x: x.time, reverse=True)
for i in events_sorted:
    i.show()


# среднее число каналов в обслуживании равно среднему числу обслуживаемых заявок
lam = round((1/interval),2)

p1 = round(((lam * evm_1_w)/1),2)
p2 = round(((lam * evm_2_w)/1),2)
p3 = round(((lam * evm_3_w)/1),2)

l1 = p1*1
l2 = p2*1
l3 = p3*1

served_chanel = l1 + l2 +l3


# среднее число заявок в очереди можно найти по формуле L_оч = (p^2 * (1 - p)) / (2 * (1 - p)),
# где p - вероятность того, что заявка приходит в систему и не обслуживается сразу же.
r = 1 - weight_1
task_in_queue = (r**2*(1-r))/(2*(1-r))

# среднее число заявок в системе равно сумме среднего числа заявок в очереди и среднего числа каналов в обслуживани


print('')
print('Статистика ЭВМ 1:')
print('Количество заявок:', evm_1_total_tasks)
print('Общее время работы:', round(evm_1_total_time,2),'мин.')
print('Простой ЭВМ:', round((round(evm_1_total_relax,2)/round(evm_1_total_time,2))*100,2),'%')
print('Коэффициент занятости:', round(( (evm_1_total_time - evm_1_total_relax) / evm_1_total_time),2)*100, '%')
# мы больше ждем заявок, чем они ждут в очереди, это можно увидеть во времени простоя
queue_1 = float(abs(evm_1_total_time - evm_1_total_relax - evm_1_total_queue) / evm_1_total_tasks)
print('Среднее время ожидания в очереди', round(queue_1,3),'мин.')

print('')
print('Статистика ЭВМ 2:')
print('Количество заявок:', evm_2_total_tasks)
print('Общее время работы:', round(evm_2_total_time,2),'мин.')
print('Простой ЭВМ:', round((round(evm_2_total_relax,2)/round(evm_2_total_time,2))*100,2),'%')
print('Коэффициент занятости:', round(((evm_2_total_time - evm_2_total_relax) / evm_2_total_time),2)*100, '%')
# мы больше ждем заявок, чем они ждут в очереди, это можно увидеть во времени простоя
queue_2 = float(abs(evm_2_total_time - evm_2_total_relax - evm_2_total_queue) / evm_2_total_tasks)
print('Среднее время ожидания в очереди', round(queue_2,2),'мин.')

print('')
print('Статистика ЭВМ 3:')
print('Количество заявок:', evm_3_total_tasks)
print('Общее время работы:', round(evm_3_total_time,2),'мин.')
print('Простой ЭВМ:', round((round(evm_3_total_relax,2)/round(evm_3_total_time,2))*100,2),'%')
print('Коэффициент занятости:', round(((evm_3_total_time - evm_3_total_relax) / evm_3_total_time),2)*100, '%')
# мы больше ждем заявок, чем они ждут в очереди, это можно увидеть во времени простоя
queue_3 = float(abs(evm_3_total_time - evm_3_total_relax - evm_3_total_queue) / evm_3_total_tasks)
print('Среднее время ожидания в очереди', round(queue_3,2),'мин.')



print('')
print("Общая статистика работы системы:")
print('Время работы системы:', round(events_sorted[0].time - events_sorted[len(events_sorted) - 1].time,2),'мин.')
print('Среднее число каналов в обслуживании:', round(served_chanel))
print('Среднее число заявок в очереди:', round(task_in_queue))
print('Среднее число заявок в системе:', round(round(served_chanel)+round(task_in_queue)))
print('Среднее время пребывания заявки в системе:',round( (evm_1_total_relax + evm_2_total_relax + evm_3_total_relax) / (
        evm_1_total_tasks + evm_2_total_tasks + evm_3_total_tasks),2),'мин.')
print('Среднее время ожидания в очереди', round (((queue_1 + queue_2 + queue_3) / 3.0),2),'мин.')
#print('Эффективность', tasks / (events_sorted[0].time - events_sorted[len(events_sorted) - 1].time))


# РЕКОМЕНДАЦИИ
# ЗАВИСЯТ ОТ ВХОДНЫХ ДАННЫХ
# Направить больше заявок на ЭВМ_2 и ЭВМ_3, так как ЭВМ_1 работает, но все равно отдает заяки на ЭВМ_2 и ЭВМ_3, в идеале необходимо свести это количество к нулю;
# При этом изменить распределение из ЭВМ_1 в ЭВМ_2 и ЭВМ_3 на [0.8:0.2], так как ЭВМ_2 работает быстрее ЭВМ_3;


