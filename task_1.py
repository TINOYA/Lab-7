import numpy as np
import random
import time

# Создание двух массивов в 1 миллион элементов, заполненных случайными значениями чиселee
lst1 = [random.random() for _ in range(1000000)]
lst2 = [random.random() for _ in range(1000000)]
arr1 = np.array(lst1)
arr2 = np.array(lst2)

# Измерение времени выполнения операции поэлементного перемножения стандартных списков
start_time = time.perf_counter()
result_lst = [x * y for x, y in zip(lst1, lst2)]
end_time = time.perf_counter()
total_time_lst = end_time - start_time
print(f"Время выполнения операции поэлементного перемножения стандартных списков: {total_time_lst} секунд")

# Измерение времени выполнения операции поэлементного перемножения массивов NumPy
start_time = time.perf_counter()
result_arr = np.multiply(arr1, arr2)
end_time = time.perf_counter()
total_time_arr = end_time - start_time
print(f"Время выполнения операции поэлементного перемножения массивов NumPy: {total_time_arr} секунд")

# Сравнение времени выполнения
if total_time_lst < total_time_arr:
    print("Стандартные списки быстрее")
else:
    print("Массивы NumPy быстрее")