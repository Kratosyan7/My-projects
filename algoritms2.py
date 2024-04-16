import matplotlib.pyplot as plt
import numpy as np

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def visualize_sorting(arr):
    merge_sort(arr)
    plt.bar(range(len(arr)), arr, color='b')
    plt.title('Сортировка слиянием')
    plt.show()

# Пример использования
if __name__ == "__main__":
    arr = np.random.randint(1, 50, 10)  # Генерация случайного массива
    print("Исходный массив:", arr)
    visualize_sorting(arr.copy())  # Копируем массив для визуализации, иначе он отсортируется