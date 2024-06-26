"""
Лабораторная работа №7 с графическим интерфейсом по заданию из ЛР №6:
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу,
введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 25. У няни неограниченное количество  фруктов К разных названий (ф1,…фК).
Сформировать (вывести) все возможные варианты меню полдника (N фруктов) для ребенка на неделю.
"""

import tkinter as tk
from tkinter import scrolledtext, ttk
import itertools
import timeit
import random
"""
Определяем функцию для генерации всех возможных меню (алгоритмический подход)
"""
def generate_menus_alg(fruits, N):
    if N == 0:
        yield []
    else:
        for m in fruits:
            for rest_of_menu in generate_menus_alg(fruits, N - 1):
                yield [m] + rest_of_menu



def generate_menus_func(fruits, N):
    return list(itertools.product(fruits, repeat=N))

def is_valid_menu(menu):
    return all(menu[i] != menu[i + 1] for i in range(len(menu) - 1))

def diversity_score(menu):
    return len(set(menu))

def generate_menus_with_constraints(fruits, N, generator_function):
    max_diversity = 0
    optimal_menus = []

    for menu in generator_function(fruits, N):
        if is_valid_menu(menu):
            diversity = diversity_score(menu)
            if diversity > max_diversity:
                max_diversity = diversity
                optimal_menus = [menu]
            elif diversity == max_diversity:
                optimal_menus.append(menu)

    return optimal_menus
"""
Функция вызываемая при нажатии кнопки
"""
def generate_and_display_menus():
    global menus
    try:
        K = int(entry_k.get())
        if K <=0:
            raise ValueError("Число должно быть больше нуля.")

    except ValueError as e:
        text_area.insert(tk.INSERT, f"Некорректный ввод: {e}. Пожалуйста, попробуйте снова.\n")
        return
    N = 7
    fruits = [f'ф{i+1}' for i in range(K)]
    selected_method = method_var.get()
    """
    Очистка текстового поля
    """
    text_area.delete('1.0', tk.END)
    """
    Выбор метода генерации
    """

    if selected_method == 'Алгоритмический':
        start_time = timeit.default_timer()
        menus = list(generate_menus_alg(fruits, N))
        time_taken = timeit.default_timer() - start_time
        text_area.insert(tk.INSERT, f"Метод: {selected_method}\n")
        text_area.insert(tk.INSERT, f"Сгенерировано {len(menus)} меню.\n")
        if menus:
            sample_size = min(5, len(menus))
            random_menus = random.sample(menus, sample_size)
            example_menus = format_menus_for_display(random_menus)
            text_area.insert(tk.INSERT, f"Примеры меню:\n{example_menus}\n")
        else:
            text_area.insert(tk.INSERT, "Нет меню\n")


    elif selected_method == 'Функциональный':
        start_time = timeit.default_timer()
        menus = generate_menus_func(fruits, N)
        time_taken = timeit.default_timer() - start_time
        text_area.insert(tk.INSERT, f"Метод: {selected_method}\n")
        text_area.insert(tk.INSERT, f"Сгенерировано {len(menus)} меню.\n")
        if menus:
            sample_size = min(5, len(menus))
            random_menus = random.sample(menus, sample_size)
            example_menus = format_menus_for_display(random_menus)
            text_area.insert(tk.INSERT, f"Примеры меню:\n{example_menus}\n")
        else:
            text_area.insert(tk.INSERT, "Нет меню\n")
    elif selected_method == 'Алгоритмический с ограничениями':
        start_time = timeit.default_timer()
        menus = list(generate_menus_alg(fruits, N))
        optimal_menus = generate_menus_with_constraints(fruits, N, lambda x, y: menus)
        time_taken = timeit.default_timer() - start_time
        text_area.insert(tk.INSERT, f"Метод: {selected_method}\n")
        text_area.insert(tk.INSERT, f"Сгенерировано {len(optimal_menus)} оптимальных меню с ограничениями.\n")
        if optimal_menus:
            sample_size = min(5, len(optimal_menus))
            random_optimal_menus = random.sample(optimal_menus, sample_size)
            example_menus = format_menus_for_display(random_optimal_menus)
            text_area.insert(tk.INSERT, f"Примеры меню:\n{example_menus}\n")
        else:
            text_area.insert(tk.INSERT, "Нет меню\n")
        max_diversity = max(map(diversity_score, optimal_menus), default=0)
        text_area.insert(tk.INSERT, f"Максимальное разнообразие фруктов в оптимальных меню: {max_diversity}\n")
    elif selected_method == 'Функциональный с ограничениями':
        start_time = timeit.default_timer()
        menus = generate_menus_func(fruits, N)
        optimal_menus = generate_menus_with_constraints(fruits, N, generate_menus_func)
        time_taken = timeit.default_timer() - start_time
        text_area.insert(tk.INSERT, f"Метод: {selected_method}\n")
        text_area.insert(tk.INSERT, f"Сгенерировано {len(optimal_menus)} оптимальных меню с ограничениями.\n")
        if optimal_menus:
            sample_size = min(5, len(optimal_menus))
            random_optimal_menus = random.sample(optimal_menus, sample_size)
            example_menus = format_menus_for_display(random_optimal_menus)
            text_area.insert(tk.INSERT, f"Примеры меню:\n{example_menus}\n")
        else:
            text_area.insert(tk.INSERT, "Нет меню\n")
        max_diversity = max(map(diversity_score, optimal_menus), default=0)
        text_area.insert(tk.INSERT, f"Максимальное разнообразие фруктов в оптимальных меню: {max_diversity}\n")
    else:
        text_area.insert(tk.INSERT, "Неподдерживаемый метод генерации.\n")
        return

    text_area.insert(tk.INSERT, f"Время выполнения: {time_taken:.6f} секунд\n\n")

def format_menus_for_display(menus):
    return '\n'.join(', '.join(menu) for menu in menus)

"""
Создание основного окна
"""
root = tk.Tk()
root.title("Генератор меню полдника")
"""
Определение стилей
"""
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', background='#FF5733', foreground='black', font=('Helvetica', 12, 'bold'))
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TFrame', background='#D5E8D4')
"""
Создание фреймов для разделения интерфейса
"""
input_frame = ttk.Frame(root, padding="10 10 10 10", style='TFrame')
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

output_frame = ttk.Frame(root, padding="10 10 10 10", style='TFrame')
output_frame.pack(padx=10, pady=10, fill='both', expand=True)
"""
Ввод количества фруктов K
"""
label_k = ttk.Label(input_frame, text="Введите общее количество различных фруктов (K):", background='#D5E8D4')
label_k.pack(side='left', padx=5, pady=5)

entry_k = ttk.Entry(input_frame, width=30)
entry_k.pack(side='left', padx=5, pady=5)
"""
Выбор метода генерации
"""
method_var = tk.StringVar()
method_label = ttk.Label(input_frame, text="Выберите метод генерации:", background='#D5E8D4')
method_label.pack(side='left', padx=5, pady=5)

method_dropdown = ttk.Combobox(input_frame, textvariable=method_var, values=[
    'Алгоритмический',
    'Функциональный',
    'Алгоритмический с ограничениями',
    'Функциональный с ограничениями'
], state="readonly", width=20)
method_dropdown.pack(side='left', padx=5, pady=5)
method_dropdown.current(0)

generate_button = ttk.Button(input_frame, text="Сгенерировать меню", command=generate_and_display_menus)
generate_button.pack(side='left', padx=5, pady=5)
"""
Виджет для вывода результатов
"""
text_area = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, font=('Helvetica', 12), width=60, height=10)
text_area.pack(padx=10, pady=10, fill='both', expand=True)
"""
Запускаем главный цикл Tkinter
"""
root.mainloop()
