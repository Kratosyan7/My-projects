import matplotlib.pyplot as plt
import numpy as np
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr  # Возвращаем массив после каждой замены

def visualize_sorting(arr):
    fig, ax = plt.subplots()
    ax.set_title('Сортировка пузырьком')
    bar_rects = ax.bar(range(len(arr)), arr, color='b', align='edge')
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * len(arr)))

    iteration = [0]  # Количество итераций

    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        ax.set_title(f'Сортировка пузырьком (Итерация {iteration[0]})')

    for sorted_arr in bubble_sort(arr):
        update_fig(sorted_arr, bar_rects, iteration)
        plt.pause(0.05)  # Пауза для обновления графика

    plt.show()

# Пример использования
if __name__ == "__main__":
    arr = np.random.randint(1, 50, 10)  # Генерация случайного массива
    print("Исходный массив:", arr)
    visualize_sorting(arr.copy())  # Копируем массив для визуализации, иначе он отсортируется