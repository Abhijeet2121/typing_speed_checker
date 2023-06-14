from  tkinter import *
import tkinter as tk
import time
import random
import threading

class TypeSpeed:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("900x700")
        self.window.title("Check Typing Speed")
        self.window.config(padx=50, pady=50)

        self.text = open("text.txt", 'r').read().split('\n')

        self.start_button = Button(self.window, text="Test Your Typing Speed",
                            padx=20, pady=10, highlightthickness=0,
                            anchor="w", command=self.start)
        self.start_button.grid(row=0, column=0, sticky='w')

        self.sample_text_label = Label(self.window, text=random.choice(self.text), font=("Helventica", 16),
                                 anchor='w')
        self.sample_text_label.grid(row=1, column=0, padx=20, pady=10, sticky='w')

        self.text_entry = Entry(self.window, font=("Helventica", 18), width=60)
        self.text_entry.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        self.text_entry.bind('<KeyPress>', self.check_text)

        self.speed_label = Label(self.window, text=" Speed: \n 0:00 CPS \n 0:00 CPM \n 0:00 WPS \n 0:00 WPM ",font=("Heventical", 20),
                            width=20, anchor='w')
        self.speed_label.grid(row=3, column=0, padx=20, pady=10, sticky='w')

        self.reset_button = Button(self.window, text="Reset",
                            padx=20, pady=10, highlightthickness=0,
                            anchor='w', command=self.reset)
        self.reset_button.grid(row=4, column=0, sticky='w')
        
        self.counter = 0
        self.running = False

        self.window.mainloop()

    def start(self):
        if not self.running:
            self.running = True
            t = threading.Thread(target=self.time_thread)
            t.start()
            
    def check_text(self, event):
        if not self.sample_text_label.cget('text') == self.text_entry.get():
            self.text_entry.config(fg="red")
        else:
            self.text_entry.config(fg="green")
            self.running = False

    def time_thread(self):
        while self.running:
            time.sleep(0.01)
            self.counter += 0.01
            cps = len(self.text_entry.get())/ self.counter
            cpm = cps * 60
            wps = len(self.text_entry.get().split(" "))/ self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n {cps:.2f} CPS \n {cpm:.2f} CPM \n {wps:.2f} WPS \n {wpm:.2f} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n 0:00 CPS \n 0.00 CPM \n 0.00 WPS \n 0:00 WPM")
        self.sample_text_label.config(text=random.choice(self.text))
        self.text_entry.delete(0, END)

TypeSpeed()



