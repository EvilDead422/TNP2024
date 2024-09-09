import tkinter as tk

import frames as fr
import configuration as co


class MainWindow(tk.Tk):  # Main Window that frames will be attached to from widgets.py
    def __init__(self):
        super().__init__()
        # Basic Window settings (color and size and placement)
        self.configure(background=co.DEF_COLORS['BLUE'])
        self.title('Ticket Note Pro 5')
        self.geometry('635x195')
        # self.resizable(width=False, height=False) < Uncomment this when layouts are completed

        # Some Default variables for the Window Class:
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        # Configuring columns to be the same size
        self.columnconfigure(0, weight=80)
        self.columnconfigure(1, weight=20)
        self.rowconfigure(0, weight=49)
        self.rowconfigure(1, weight=49)
        self.rowconfigure(2, weight=2)

        # Creating MAINWINDOW widgets
        self.form_group_1 = wi.FormButtonFrame(self)
        self.form_group_2 = wi.FormButtonFrame(self)
        self.entry_group = wi.EntryButtonFrame(self)
        self.menu_bar = wi.MenuFrame(self)

        # Allocating all buttons, labels, and entries to main window variables
        self.labels = [self.form_group_1.labels, self.form_group_2.labels]
        self.entries = [self.form_group_1.entries, self.form_group_2.entries, self.entry_group.entries]
        self.buttons = [self.form_group_1.buttons, self.form_group_2.buttons, self.entry_group.buttons]

        # Initial Layout (subject to change)
        self.largest_layout()

        # Testing Button Configuration:
        # self.menu.settings_button.bind('<Button-1>', command=self.open_settings) < This is failing when I run

        # Binding the Resize event to MainWindow:
        self.bind('<Configure>', self.layout_manager)

        # Calling the Main Loop inside the class for convenience
        self.mainloop()

    def layout_manager(self, _):
        pass

    def open_settings():
        pass

    def largest_layout(self):
        self.form_group_1.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
        self.form_group_2.grid(row=1, column=0, sticky='nsew', padx=2, pady=2, columnspan=2)
        self.entry_group.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
        self.menu_bar.grid(row=2, column=0, sticky='nsew', padx=2, pady=2, columnspan=2)

    '''
   Short and Wide Layouts:
   Max Width: 635
   Max Heighth: unlimited
   Short and Wide Layouts:
       1/3rd of screen / short and wide size: '635x195'
       1/2 of the size of the short wide version: '420x195'
   Tall and Thin Layouts:
       1/2 of the height of the screen and thin: '350x550'
       1/4 of the height of the screen and thin: '320x195'
   Unlimited Layout:
       > 550 pixels: Tall layout that adds fields every so many pixels....
   '''


class SettingsWindow(tk.Toplevel):
    def __init__(self):
        super().__init__(background=co.DEF_COLORS['BLUE'])

        self.central = fr.SettingsFrame(self)

    def open_label_edit(self):
        pass


class LabelWindow(tk.Toplevel):
    def __init__(self):
        super().__init__(background=co.DEF_COLORS['BLUE'])

        self.central = fr.LabelFrame(self, co.DEF_LABELS)

    def save_labels(self):
        pass


MainWindow()
