''' Задача 1
import random
import requests


def get_random():
    response = requests.get("https://type.fit/api/quotes")
    сitations = response.json()
    random_сitation = random.choice(сitations)
    return random_сitation

def print_сitation(сitation):
    print("Цитата:")
    print(сitation["text"])
    print("Автор:")
    print(сitation["author"])

def main():
    сitation = get_random()
    print_сitation(сitation)

main()
'''

























''' Задача 2
import tkinter as tk

root = tk.Tk()
root.title("Логотип Dinur")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

center_x = 150
center_y = 150

canvas.create_polygon(center_x, center_y - 100, center_x + 100, center_y, center_x, center_y + 100, center_x - 100, center_y, fill="orange", outline="black", width=2)

text_x = center_x
text_y = center_y

canvas.create_text(text_x, text_y, text="Dinur", font=("Helvetica", 24), fill="black")

root.mainloop()
'''