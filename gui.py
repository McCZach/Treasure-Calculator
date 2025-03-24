from tables.potions import Potion
from tables.rings import Ring
from tables.scrolls import Scroll
from tables.wands import Wand
from tables.armor import Armor

import tkinter as tk
from tkinter import scrolledtext
from tkinter import font

class Application():
    def __init__(self):
        self.__item_counts = {"Total":0, "Potion":0, "Ring":0, "Scroll":0, "Wand":0,"Armor":0}

        self.__main_window = tk.Tk()
        self.__main_window.geometry('1000x800')
        self.__main_window.title('Treasure Generator')

        # Setup Application
        self.__option_frame = tk.Frame(self.__main_window)
        self.__option_frame.pack()

        self.__display_frame = tk.Frame(self.__main_window, border=6, relief='sunken')
        self.__display_frame.pack()

        self.__display_text = scrolledtext.ScrolledText(self.__display_frame, height=30, width=100)
        self.__display_font = ("Courier", 10, "bold")
        self.__display_text.tag_configure('red_bg', background='#ff886e', font=self.__display_font)
        self.__display_text.tag_configure('orange_bg', background='#ffb46e', font=self.__display_font)
        self.__display_text.tag_configure('yellow_bg', background='#f8ff6e', font=self.__display_font)
        self.__display_text.tag_configure('green_bg', background='#80ff6e', font=self.__display_font)
        self.__display_text.tag_configure('blue_bg', background='#6e84ff', font=self.__display_font)
        self.__display_text.config(state=tk.DISABLED)
        self.__display_text.pack()

        # Create Result Area
        self.__result_frame = tk.Frame(self.__main_window)
        self.__result_frame.pack()

        self.__item_labels = {
            "Total":tk.Label(self.__result_frame),
            "Potion":tk.Label(self.__result_frame),
            "Ring":tk.Label(self.__result_frame),
            "Scroll":tk.Label(self.__result_frame),
            "Wand":tk.Label(self.__result_frame),
            "Armor":tk.Label(self.__result_frame),
        }

        for label in self.__item_labels:
            self.__item_labels[label].pack()

        self.__buttons = {
            "Potion":tk.Button(self.__option_frame, text='Generate Potion', 
                    command=lambda: self.display_item(Potion.generate_potion, 'Potion', 'red_bg', self.__item_labels['Potion'])),
            "Ring":tk.Button(self.__option_frame, text='Generate Ring',
                    command=lambda: self.display_item(Ring.generate_ring, 'Ring', 'orange_bg', self.__item_labels['Ring'])),
            "Scroll":tk.Button(self.__option_frame, text='Generate Scroll',
                    command=lambda: self.display_item(Scroll.generate_scroll, 'Scroll', 'yellow_bg',self.__item_labels['Scroll'])),
            "Wand":tk.Button(self.__option_frame, text='Generate Rod/Staff/Wand',
                    command=lambda: self.display_item(Wand.generate_wand, 'Wand', 'green_bg', self.__item_labels['Wand'])),
            "Armor":tk.Button(self.__option_frame, text='Generate Armor',
                    command=lambda: self.display_item(Armor.generate_armor, 'Armor', 'blue_bg', self.__item_labels['Armor'])),
            "Clear":tk.Button(self.__option_frame, text='Clear', 
                    command=lambda: self.clear_text())
        }

        for button in self.__buttons:
            self.__buttons[button].pack(side='left', padx=5)

        tk.mainloop()

    def clear_text(self):
        self.__display_text.config(state=tk.NORMAL)
        self.__display_text.delete("1.0", tk.END)
        self.__display_text.config(state=tk.DISABLED)

        for count in self.__item_counts:
            self.__item_counts[count] = 0

        self.__item_labels['Total'].config(text=f'Number of Items: {self.__item_counts["Total"]}')
        self.__item_labels['Potion'].config(text=f'Number of Potions: {self.__item_counts["Potion"]}')
        self.__item_labels['Ring'].config(text=f'Number of Rings: {self.__item_counts["Ring"]}')
        self.__item_labels['Scroll'].config(text=f'Number of Scrolls: {self.__item_counts["Scroll"]}')
        self.__item_labels['Wand'].config(text=f'Number of Wands: {self.__item_counts["Wand"]}')
        self.__item_labels['Armor'].config(text=f'Number of Armor: {self.__item_counts["Armor"]}')

    def display_item(self, generate, name, bg, box):
        item = generate()
        self.__display_text.config(state=tk.NORMAL)
        self.__display_text.insert(tk.END, item, bg)
        self.__display_text.config(state=tk.DISABLED)

        self.__item_counts['Total'] += 1
        self.__item_labels['Total'].config(text=f'Number of Items: {self.__item_counts['Total']}')
        self.__item_counts[name] += 1
        box.config(text=f'Number of {name}: {self.__item_counts[name]}')