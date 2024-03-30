#Вариант 25 Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
#Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
# F(1) = 4; F(2) = 5; F(n) = (-1)n*(F(n-1)- F(n-2) /(2n)!) при n > 2.
import math
import time
import matplotlib.pyplot as plt

# Функция для рекурсивного вычисления
def recursive_F(n):
    if n == 1:
        return 4
    elif n == 2:
        return 5
    else:
        return ((-1)**n) * (recursive_F(n-1) - recursive_F(n-2)) / math.factorial(2*n)

# Функция для итерационного вычисления
def iterative_F(n):
    if n == 1:
        return 4
    elif n == 2:
        return 5
    else:
        F_n_minus_1 = 5
        F_n_minus_2 = 4
        fact = math.factorial(4)
        for i in range(3, n + 1):
            fact *= (2*i - 1) * (2*i)
            F_n = ((-1)**i) * (F_n_minus_1 - F_n_minus_2) / fact
            F_n_minus_2, F_n_minus_1 = F_n_minus_1, F_n
        return F_n_minus_1

# Сравнительное исследование времени вычисления
def compare_methods(max_n):
    recursive_times = []
    iterative_times = []
    ns = range(1, max_n + 1)
    for i in ns:
        start_time = time.perf_counter()
        recursive_F(i)
        recursive_times.append(time.perf_counter() - start_time)

        start_time = time.perf_counter()
        iterative_F(i)
        iterative_times.append(time.perf_counter() - start_time)

    return ns, recursive_times, iterative_times

# Визуализация результатов
def plot_results(ns, recursive_times, iterative_times):
    plt.plot(ns, recursive_times, label='Рекурсивный')
    plt.plot(ns, iterative_times, label='Итерационный')
    plt.xlabel('n')
    plt.ylabel('Время (секунды)')
    plt.yscale('log')
    plt.legend()
    plt.title('Сравнительное исследование рекурсивного и итерационного вычислений')
    plt.grid(True)
    plt.show()


# Главная функция для запуска сравнения и визуализации
def main():
    max_n = 10
    ns, recursive_times, iterative_times = compare_methods(max_n)
    plot_results(ns, recursive_times, iterative_times)


if __name__ == "__main__":
    main()