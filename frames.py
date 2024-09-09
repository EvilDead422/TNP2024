import customtkinter as ctk
import configuration as co
from PIL import Image

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')


class FormButtonFrame(ctk.CTkFrame):  # Represents the most common widget frame in the application window (TNP5.exe)
    def __init__(self, parent):  # primary_color, secondary_color, tertiary_color, text_color, text
        super().__init__(master=parent)
        # Instancing the main lists for the individual smaller widgets
        self.labels = []
        self.entries = []
        self.buttons = []

        # configuring columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=98)
        self.columnconfigure(2, weight=1)

        # Adding smaller widgets to the frame by appending them to the lists and using grid to place.
        for num in range(4):
            self.rowconfigure(num, weight=1)  # Configure all rows in the loop to save space
            self.labels.append(ctk.CTkLabel(self, text=f'Label-{num + 1}:', font=('Cambria', 12)))
            self.labels[num].grid(row=num, column=0, padx=2)
            self.entries.append(ctk.CTkEntry(self, width=120, height=20))
            self.entries[num].grid(row=num, column=1, sticky='ew')
            self.buttons.append(ctk.CTkButton(self, text='COPY', font=('Cambria', 10), width=50, height=20))
            self.buttons[num].grid(row=num, column=2, padx=2)


class EntryButtonFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        # Instancing the main lists for the individual smaller widgets
        self.entries = []
        self.buttons = []

        # configuring columns
        self.columnconfigure(0, weight=99)
        self.columnconfigure(1, weight=1)

        # Adding smaller widgets to the frame by appending them to the lists and using grid to place.
        for num in range(4):
            self.rowconfigure(num, weight=1)  # Configure all rows in the loop to save space
            self.entries.append(ctk.CTkEntry(self, width=120, height=20))
            self.entries[num].grid(row=num, column=0, sticky='ew', padx=3)
            self.buttons.append(ctk.CTkButton(self, text='COPY', font=('Cambria', 10), width=50, height=20))
            self.buttons[num].grid(row=num, column=1, padx=2)


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=98)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        self.settings_image = ctk.CTkImage(light_image=Image.open('settings.png'),
                                           dark_image=Image.open('settings.png'))
        self.settings_button = ctk.CTkLabel(self, text='', image=self.settings_image, width=50, height=20)
        self.time_label = ctk.CTkLabel(self, text=co.TIME_TEST, width=50, height=20, font=('Cambria', 14))
        self.clear_all = ctk.CTkButton(self, text='Clear All', width=50, height=20, font=('Cambria', 10),
                                       hover_color='red')

        self.settings_button.grid(row=0, column=0)
        # self.settings_button.bind("<Button-1>" (Left Mouse Button), %Command%)
        self.time_label.grid(row=0, column=1)
        self.clear_all.grid(row=0, column=2, padx=2)


class LabelFrame(ctk.CTkFrame):
    def __init__(self, parent, values):
        super().__init__(master=parent)

        self.entries = []

        for num in range(8):
            self.entries.append(ctk.CTkEntry(self, width=120, height=20))
            self.entries[num].grid(row=num, column=1, sticky='ew')
            self.entries[num].insert(0, values[num])


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        pass




