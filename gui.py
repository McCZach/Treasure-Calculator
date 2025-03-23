from tables.potions import Potion
from tables.rings import Ring
from tables.scrolls import Scroll

import tkinter as tk
from tkinter import scrolledtext

class Application():
    def __init__(self):
        self.__num_items = 0
        self.__xp_amount = 0
        self.__gold_amount = 0

        self.__main_window = tk.Tk()
        self.__main_window.geometry('800x600')
        self.__main_window.title('Treasure Generator')

        # Setup Application
        self.__option_frame = tk.Frame(self.__main_window)
        self.__option_frame.pack()

        self.__display_frame = tk.Frame(self.__main_window, border=6, relief='sunken')
        self.__display_frame.pack()

        self.__display_text = scrolledtext.ScrolledText(self.__display_frame, height=30, width=80)
        self.__display_text.tag_configure("red_bg", background='tomato')
        self.__display_text.tag_configure("orange_bg", background='orange')
        self.__display_text.tag_configure("yellow_bg", background='burlywood1')
        self.__display_text.pack()

        # Create Result Area
        self.__result_frame = tk.Frame(self.__main_window)
        self.__result_frame.pack()

        self.__items = tk.Label(self.__result_frame)
        self.__items.pack()

        # Create Buttons
        self.__generate_potion = tk.Button(self.__option_frame, text='Generate Potion', 
                                           command=lambda: self.display_potion())
        self.__generate_potion.pack(side='left', padx=5)

        self.__generate_ring = tk.Button(self.__option_frame, text='Generate Ring',
                                        command=lambda: self.display_ring())
        self.__generate_ring.pack(side='left', padx=5)

        self.__generate_scroll = tk.Button(self.__option_frame, text='Generate Scroll',
                                           command=lambda: self.display_scroll())
        self.__generate_scroll.pack(side='left', padx=5)

        self.__clear_button = tk.Button(self.__option_frame, text='Clear', 
                                        command=lambda: self.clear_text())
        self.__clear_button.pack(side='left', padx=5)

        tk.mainloop()

    def clear_text(self):
        self.__display_text.delete("1.0", tk.END)

    def display_potion(self):
        potion = Potion.generate_potion()
        self.__display_text.insert(tk.END, potion, 'red_bg')

        self.__num_items += 1
        self.__items.config(text=f'Number of Items: {self.__num_items}')

    def display_ring(self):
        ring = Ring.generate_ring()
        self.__display_text.insert(tk.END, ring, 'orange_bg')

        self.__num_items += 1
        self.__items.config(text=f'Number of Items: {self.__num_items}')

    def display_scroll(self):
        scroll = Scroll.generate_scroll()
        self.__display_text.insert(tk.END, scroll, 'yellow_bg')

        self.__num_items += 1
        self.__items.config(text=f'Number of Items: {self.__num_items}')