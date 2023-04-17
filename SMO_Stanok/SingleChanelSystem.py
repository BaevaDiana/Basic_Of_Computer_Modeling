import random
import numpy as np

details = 500 # количество деталей
time = 0 # время выполнения
time_issues = 0 #
breakage_interval = np.random.normal(20, 2) # интервалы между поломками
processing_time = 0 #время обработки
queue = []
expectation = 0
count_breakdown = 0 # количество поломок
troubleshooting_issues_total_time = 0 # общее время исправления поломок

time_entrance = [] # время поступления детали в станок
interval_entrance = []

for i in range(details):
    entrance = random.expovariate(1)
    if i == 0:
        time_entrance.append(entrance)
    else:
        time_entrance.append(entrance + time_entrance[-1])
    interval_entrance.append(entrance)


# print(time_entrance)

# проверка станка на поломку
def check_breakage(setting_up):
    global time, processing_time
    if breakage_interval <= 0:
        time += setting_up + breakage_interval
        processing_time += setting_up + breakage_interval
        breakdown()
        return True
    else:
        time += setting_up
        processing_time += setting_up
        return False

# обработка поломки станка
def breakdown():
    global breakage_interval, time, processing_time, time_issues
    breakage_interval = np.random.normal(20, 2)
    troubleshooting_issues = np.random.uniform(0.1, 0.5)
    time += troubleshooting_issues
    time_issues += troubleshooting_issues
    processing_time += troubleshooting_issues


i = 0
obrabotka = 0

while i != details:
    if i == 0:
        time += time_entrance[0]
    else:
        if time < time_entrance[i]:
            time += time_entrance[i] - time

    #print(i + 1)
   # print('Время поступления детали в станок:',round(time_entrance[i]),'ч.')
    #print('Обработка детали...')
    setting_up = np.random.uniform(0.2, 0.5) # наладка станка
    breakage_interval -= setting_up

    #print('Наладка станка:', round(setting_up,3),'ч.')
    if check_breakage(setting_up):
        i -= 1
        #print('Поломка!')
        count_breakdown += 1

    task_execution = np.random.normal(0.5, 0.1)
    breakage_interval -= task_execution

    if check_breakage(task_execution):
        i -= 1
        #print('Поломка!')
        count_breakdown += 1

    i += 1
    #print('Время выполнения задания:', round(task_execution,3),'ч.')
    #print('Время обработки детали всего:', round(processing_time,3),'ч.')
    obrabotka += processing_time
    #print('Время работы станка:',round(time),'ч.')
    processing_time = 0
    #print("До поломки осталось: ", round(breakage_interval),'ч.')
    #print()

print('---------------------------------------------------------------------')
print('Итоговое время работы станка:', round(time),'ч.')
print('Среднее время поступления деталей:', round((sum(interval_entrance) / details),3),'ч.')
print('Количество поломок:', count_breakdown)
print('Время, затраченное на исправление поломок:', round(time_issues),'ч.')
print('---------------------------------------------------------------------')
