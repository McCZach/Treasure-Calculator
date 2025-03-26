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
        #****************************************************************************************

        self.main_window = tk.Tk()
        self.main_window.geometry('1000x800')
        self.main_window.title('Treasure Generator')

        self.option_frame = tk.Frame(self.main_window)
        self.option_frame.pack()

        self.display_frame = tk.Frame(self.main_window, border=6, relief='sunken')
        self.display_frame.pack()

        self.result_frame = tk.Frame(self.main_window)
        self.result_frame.pack()

        #****************************************************************************************

        self.counts = {'Total':0, 'Potion':0, 'Ring':0, 'Scroll':0, 'Wand':0, 'Armor':0}

        self.create_buttons()
        self.create_text()
        self.create_labels()

        #****************************************************************************************

        tk.mainloop()

    def create_buttons(self):
        self.buttons = {
            "Potion":tk.Button(self.option_frame, text='Generate Potion', 
                    command=lambda: self.display_item(Potion.generate_potion, 'Potion', 'red_bg', self.labels['Potion'])),
            "Ring":tk.Button(self.option_frame, text='Generate Ring',
                    command=lambda: self.display_item(Ring.generate_ring, 'Ring', 'orange_bg', self.labels['Ring'])),
            "Scroll":tk.Button(self.option_frame, text='Generate Scroll',
                    command=lambda: self.display_item(Scroll.generate_scroll, 'Scroll', 'yellow_bg',self.labels['Scroll'])),
            "Wand":tk.Button(self.option_frame, text='Generate Rod/Staff/Wand',
                    command=lambda: self.display_item(Wand.generate_wand, 'Wand', 'green_bg', self.labels['Wand'])),
            "Armor":tk.Button(self.option_frame, text='Generate Armor',
                    command=lambda: self.display_item(Armor.generate_armor, 'Armor', 'blue_bg', self.labels['Armor'])),
            "Clear":tk.Button(self.option_frame, text='Clear', 
                    command=lambda: self.clear_text())
        }

        for button in self.buttons:
            self.buttons[button].pack(side='left', padx=5)

    def create_labels(self):
        self.label_vars = {
            'Total':tk.StringVar(),
            'Potion':tk.StringVar(),
            'Ring':tk.StringVar(),
            'Scroll':tk.StringVar(),
            'Wand':tk.StringVar(),
            'Armor':tk.StringVar()
        }

        self.labels = {
            'Total':tk.Label(self.result_frame, textvariable=self.label_vars['Total']),
            'Potion':tk.Label(self.result_frame, textvariable=self.label_vars['Potion']),
            'Ring':tk.Label(self.result_frame, textvariable=self.label_vars['Ring']),
            'Scroll':tk.Label(self.result_frame, textvariable=self.label_vars['Scroll']),
            'Wand':tk.Label(self.result_frame, textvariable=self.label_vars['Wand']),
            'Armor':tk.Label(self.result_frame, textvariable=self.label_vars['Armor'])
        }

        for label in self.labels:
            self.labels[label].pack()

    def create_text(self):
        self.display_text = scrolledtext.ScrolledText(self.display_frame, height=30, width=100)
        self.display_font = ("Courier", 10, "bold")
        self.display_tags = {
            'red_bg':'#ff886e',
            'orange_bg':'#ffb46e',
            'yellow_bg':'#f8ff6e',
            'green_bg':'#80ff6e',
            'blue_bg':'#6e84ff'
        }

        for key, value in self.display_tags.items():
            self.display_text.tag_configure(key, background=value, font=self.display_font)
        del self.display_tags
        del self.display_font

        self.display_text.config(state=tk.DISABLED)
        self.display_text.pack()

    def display_item(self, generate, name, tag, box):
        item = generate()
        self.display_text.config(state=tk.NORMAL)
        self.display_text.insert(tk.END, item, tag)
        self.display_text.config(state=tk.DISABLED)

        self.counts['Total'] += 1
        self.label_vars['Total'].set(f'Number of Total Items: {self.counts['Total']}')

        self.counts[name] += 1
        self.label_vars[name].set(f'Number of {name}: {self.counts[name]}')

    def clear_text(self):
        self.display_text.config(state=tk.NORMAL)
        self.display_text.delete("1.0", tk.END)
        self.display_text.config(state=tk.DISABLED)

        for count in self.counts:
            self.counts[count] = 0

        for key in self.label_vars:
            self.label_vars[key].set(f'Number of {key}: {self.counts[key]}')