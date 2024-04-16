import tkinter as tk
from collections import deque

class Player:
    def __init__(self, name):
        self.name = name

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

locations_stack = []
tasks_queue = deque()

locations = {
    "Лес": Location("Лес", "Вы находитесь в густом лесу. Впереди разветвление тропы."),
    "Ручей": Location("Ручей", "Вы находитесь у живописного ручья. Здесь прохладно и свежо."),
    "Пещера": Location("Пещера", "Вы вошли в темную пещеру. Перед вами разветвление.")
}

tasks = [
    "Найти ключ от загадочного сундука.",
    "Решить головоломку в пещере.",
    "Найти выход из лабиринта."
]

for task in tasks:
    tasks_queue.append(task)

def complete_task():
    if tasks_queue:
        task = tasks_queue.popleft()
        tasks_listbox.delete(0)
        tasks_listbox.insert(tk.END, *tasks_queue)

def go_back():
    if len(locations_stack) > 1:
        locations_stack.pop()
        prev_location = locations_stack[-1]
        location_label.config(text=prev_location.description)

root = tk.Tk()
root.title("Путешествие в таинственный лес")

player_name = input("Введите ваше имя: ")
player = Player(player_name)

location_label = tk.Label(root, text="", wraplength=300)
location_label.pack(pady=10)

def move_to_location(location):
    location_label.config(text=location.description)

move_to_location(locations["Лес"])

tasks_frame = tk.Frame(root)
tasks_frame.pack()

tasks_label = tk.Label(tasks_frame, text="Задачи на текущий этап:")
tasks_label.grid(row=0, column=0, sticky="w")

tasks_listbox = tk.Listbox(tasks_frame, width=50, height=3)
tasks_listbox.grid(row=1, column=0, padx=10)

for task in tasks_queue:
    tasks_listbox.insert(tk.END, task)

actions_frame = tk.Frame(root)
actions_frame.pack(pady=10)

go_to_location_entry = tk.Entry(actions_frame, width=20)
go_to_location_entry.grid(row=0, column=0, padx=5)

go_to_location_button = tk.Button(actions_frame, text="Пойти в локацию", command=lambda: move_to_location(locations[go_to_location_entry.get()]))
go_to_location_button.grid(row=0, column=1, padx=5)

complete_task_button = tk.Button(actions_frame, text="Выполнить задачу", command=complete_task)
complete_task_button.grid(row=0, column=2, padx=5)

go_back_button = tk.Button(actions_frame, text="Вернуться", command=go_back)
go_back_button.grid(row=0, column=3, padx=5)

root.mainloop()