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
        self.__num_item_total = 0
        self.__num_potion = 0
        self.__num_ring = 0
        self.__num_scroll = 0
        self.__num_wand = 0
        self.__num_armor = 0

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

        self.__total_items = tk.Label(self.__result_frame)
        self.__total_items.pack()

        self.__potion_items = tk.Label(self.__result_frame)
        self.__potion_items.pack()

        self.__ring_items = tk.Label(self.__result_frame)
        self.__ring_items.pack()

        self.__scroll_items = tk.Label(self.__result_frame)
        self.__scroll_items.pack()

        self.__wand_items = tk.Label(self.__result_frame)
        self.__wand_items.pack()

        self.__armor_items = tk.Label(self.__result_frame)
        self.__armor_items.pack()

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

        self.__generate_wand = tk.Button(self.__option_frame, text='Generate Rod/Staff/Wand',
                                        command=lambda: self.display_wand())
        self.__generate_wand.pack(side='left', padx=5)

        self.__generate_armor = tk.Button(self.__option_frame, text='Generate Armor',
                                        command=lambda: self.display_armor())
        self.__generate_armor.pack(side='left', padx=5)

        self.__clear_button = tk.Button(self.__option_frame, text='Clear', 
                                        command=lambda: self.clear_text())
        self.__clear_button.pack(side='left', padx=5)

        tk.mainloop()

    def clear_text(self):
        self.__display_text.config(state=tk.NORMAL)
        self.__display_text.delete("1.0", tk.END)
        self.__display_text.config(state=tk.DISABLED)
        self.__num_item_total = 0
        self.__num_potion = 0
        self.__num_ring = 0
        self.__num_scroll = 0
        self.__num_wand = 0
        self.__num_armor = 0
        self.__total_items.config(text=f'Number of Items: {self.__num_item_total}')
        self.__potion_items.config(text=f'Number of Potions: {self.__num_potion}')
        self.__ring_items.config(text=f'Number of Rings: {self.__num_ring}')
        self.__scroll_items.config(text=f'Number of Scrolls: {self.__num_scroll}')
        self.__wand_items.config(text=f'Number of Wands: {self.__num_wand}')
        self.__armor_items.config(text=f'Number of Armor: {self.__armor_items}')

    def display_potion(self):
        potion = Potion.generate_potion()
        self.__display_text.config(state=tk.NORMAL)
        self.__display_text.insert(tk.END, potion, 'red_bg')
        self.__display_text.config(state=tk.DISABLED)

        self.__num_item_total += 1
        self.__total_items.config(text=f'Number of Items: {self.__num_item_total}')
        self.__num_potion += 1
        self.__potion_items.config(text=f'Number of Potions: {self.__num_potion}')

    def display_ring(self):
        ring = Ring.generate_ring()
        self.__display_text.config(state=tk.NORMAL)
        self.__display_text.insert(tk.END, ring, 'orange_bg')
        self.__display_text.config(state=tk.DISABLED)

        self.__num_item_total += 1
        self.__total_items.config(text=f'Number of Items: {self.__num_item_total}')
        self.__num_ring += 1
        self.__ring_items.config(text=f'Number of Rings: {self.__num_ring}')

    def display_scroll(self):
        scroll = Scroll.generate_scroll()
        self.__display_text.config(state=tk.NORMAL)
        self.__display_text.insert(tk.END, scroll, 'yellow_bg')
        self.__display_text.config(state=tk.DISABLED)

        self.__num_item_total += 1
        self.__total_items.config(text=f'Number of Items: {self.__num_item_total}')
        self.__num_scroll += 1
        self.__scroll_items.config(text=f'Number of Scrolls: {self.__num_scroll}')

    def display_wand(self):
        wand = Wand.generate_wand()
        self.__display_text.config(state=tk.NORMAL)
        self.__display_text.insert(tk.END, wand, 'green_bg')
        self.__display_text.config(state=tk.DISABLED)

        self.__num_item_total += 1
        self.__total_items.config(text=f'Number of Items: {self.__num_item_total}')
        self.__num_wand += 1
        self.__wand_items.config(text=f'Number of Wands: {self.__num_wand}')

    def display_armor(self):
        armor = Armor.generate_armor()
        self.__display_text.config(state=tk.NORMAL)
        self.__display_text.insert(tk.END, armor, 'blue_bg')
        self.__display_text.config(state=tk.DISABLED)

        self.__num_item_total += 1
        self.__total_items.config(text=f'Number of Items: {self.__num_item_total}')
        self.__num_armor += 1
        self.__armor_items.config(text=f'Number of Armor: {self.__num_armor}')