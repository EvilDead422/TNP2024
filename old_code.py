from tkinter.colorchooser import askcolor
from configparser import ConfigParser


import customtkinter as CTk
import clipboard as clip


config_file = "Config.ini"
foreground_color = "Grey"
background_color = "Black"
text_color_change = "White"
settings_window = None
ul_window = None
starting_labels = ["Label1", "Label2", "Label3", "Label4", "Label5", "Label6", "Label7", "Label8"]
ul_labels = ["Label1", "Label2", "Label3", "Label4", "Label5", "Label6", "Label7", "Label8"]




def load_colors_from_config():
   config = ConfigParser()
   config.read(config_file)
   if config.has_section("Settings"):
       # Load colors from the configuration file
       global foreground_color, background_color, text_color_change
       foreground_color = config.get("Settings", "Foreground_Color", fallback="")
       text_color_change = config.get("Settings", "Text_Color", fallback="")




def save_colors_to_config():
   config = ConfigParser()
   config.read(config_file)
   if not config.has_section("Settings"):
       config.add_section("Settings")
   # Save the colors to the configuration file
   config.set("Settings", "Foreground_Color", str(foreground_color))
   config.set("Settings", "Text_Color", str(text_color_change))
   with open(config_file, "w") as configfile:
       config.write(configfile)




def fg_color():
   global foreground_color
   foreground_color = askcolor()[1]
   if foreground_color:
       top_left.configure(fg_color=foreground_color)
       top_right.configure(fg_color=foreground_color)
       bottom.configure(fg_color=foreground_color)
       save_colors_to_config()  # Save the updated colors to the config file




def text_color():
   global text_color_change
   text_color_change = askcolor()[1]
   if text_color_change:
       label_1.configure(text_color=text_color_change)
       label_2.configure(text_color=text_color_change)
       label_3.configure(text_color=text_color_change)
       label_4.configure(text_color=text_color_change)
       label_5.configure(text_color=text_color_change)
       label_6.configure(text_color=text_color_change)
       label_7.configure(text_color=text_color_change)
       label_8.configure(text_color=text_color_change)
       save_colors_to_config()  # Save the updated colors to the config file




def copy_name():
   clip.copy(entry_1.get())




def copy_mls():
   clip.copy(entry_2.get())




def copy_agent():
   clip.copy(entry_3.get())




def copy_off():
   clip.copy(entry_4.get())




def copy_email():
   clip.copy(entry_5.get())




def copy_add():
   clip.copy(entry_6.get())




def copy_issue():
   clip.copy(entry_7.get())




def copy_category():
   clip.copy(entry_8.get())




def copy_entry_9():
   clip.copy(entry_9.get())




def copy_entry_10():
   clip.copy(entry_10.get())




def copy_entry_11():
   clip.copy(entry_11.get())




def copy_entry_12():
   clip.copy(entry_12.get())




def copy_template():
   clip.copy(starting_labels[0] + ": " + entry_1.get() + "\n" +
             starting_labels[1] + ": " + entry_2.get() + "\n" +
             starting_labels[2] + ": " + entry_3.get() + "\n" +
             starting_labels[3] + ": " + entry_4.get() + "\n" +
             starting_labels[4] + ": " + entry_5.get() + "\n" +
             starting_labels[5] + ": " + entry_6.get() + "\n" +
             starting_labels[6] + ": " + entry_7.get() + "\n" +
             starting_labels[7] + ": " + entry_8.get() + "\n")




def clear_top():
   entry_1.delete(0, 'end')
   entry_2.delete(0, 'end')
   entry_3.delete(0, 'end')
   entry_4.delete(0, 'end')
   entry_5.delete(0, 'end')
   entry_6.delete(0, 'end')
   entry_7.delete(0, 'end')
   entry_8.delete(0, 'end')




def clear_bottom():
   entry_9.delete(0, 'end')
   entry_10.delete(0, 'end')
   entry_11.delete(0, 'end')
   entry_12.delete(0, 'end')




def clear_all():
   entry_1.delete(0, 'end')
   entry_2.delete(0, 'end')
   entry_3.delete(0, 'end')
   entry_4.delete(0, 'end')
   entry_5.delete(0, 'end')
   entry_6.delete(0, 'end')
   entry_7.delete(0, 'end')
   entry_8.delete(0, 'end')
   entry_9.delete(0, 'end')
   entry_10.delete(0, 'end')
   entry_11.delete(0, 'end')
   entry_12.delete(0, 'end')




def load_labels_from_config():
   config = ConfigParser()
   config.read(config_file)
   if config.has_section("Labels"):
       # Load colors from the configuration file
       global starting_labels
       starting_labels[0] = config.get("Labels", "Label_1", fallback="")
       starting_labels[1] = config.get("Labels", "Label_2", fallback="")
       starting_labels[2] = config.get("Labels", "Label_3", fallback="")
       starting_labels[3] = config.get("Labels", "Label_4", fallback="")
       starting_labels[4] = config.get("Labels", "Label_5", fallback="")
       starting_labels[5] = config.get("Labels", "Label_6", fallback="")
       starting_labels[6] = config.get("Labels", "Label_7", fallback="")
       starting_labels[7] = config.get("Labels", "Label_8", fallback="")




def save_all_labels():
   config = ConfigParser()
   config.read(config_file)
   if not config.has_section("Labels"):
       config.add_section("Labels")
   # Save the colors to the configuration file
   config.set("Labels", "Label_1", str(starting_labels[0]))
   config.set("Labels", "Label_2", str(starting_labels[1]))
   config.set("Labels", "Label_3", str(starting_labels[2]))
   config.set("Labels", "Label_4", str(starting_labels[3]))
   config.set("Labels", "Label_5", str(starting_labels[4]))
   config.set("Labels", "Label_6", str(starting_labels[5]))
   config.set("Labels", "Label_7", str(starting_labels[6]))
   config.set("Labels", "Label_8", str(starting_labels[7]))
   with open(config_file, "w") as configfile:
       config.write(configfile)




def save_label_1():
   config = ConfigParser()
   config.read(config_file)
   if not config.has_section("Labels"):
       config.add_section("Labels")
   # Save the colors to the configuration file
   config.set("Labels", "Label_1", str(starting_labels[0]))
   with open(config_file, "w") as configfile:
       config.write(configfile)




def save_label_2():
   config = ConfigParser()
   config.read(config_file)
   if not config.has_section("Labels"):
       config.add_section("Labels")
   # Save the colors to the configuration file
   config.set("Labels", "Label_2", str(starting_labels[1]))
   with open(config_file, "w") as configfile:
       config.write(configfile)




def save_label_3():
   config = ConfigParser()
   config.read(config_file)
   if not config.has_section("Labels"):
       config.add_section("Labels")
   # Save the colors to the configuration file
   config.set("Labels", "Label_3", str(starting_labels[2]))
   with open(config_file, "w") as configfile:
       config.write(configfile)




def save_label_4():
   config = ConfigParser()
   config.read(config_file)
   if not config.has_section("Labels"):
       config.add_section("Labels")
   # Save the colors to the configuration file
   config.set("Labels", "Label_4", str(starting_labels[3]))
   with open(config_file, "w") as configfile:
       config.write(configfile)




def save_label_5():
   config = ConfigParser()
   config.read(config_file)
   if not config.has_section("Labels"):
       config.add_section("Labels")
   # Save the colors to the configuration file
   config.set("Labels", "Label_5", str(starting_labels[4]))
   with open(config_file, "w") as configfile:
       config.write(configfile)




def save_label_6():
   config = ConfigParser()
   config.read(config_file)
   if not config.has_section("Labels"):
       config.add_section("Labels")
   # Save the colors to the configuration file
   config.set("Labels", "Label_6", str(starting_labels[5]))
   with open(config_file, "w") as configfile:
       config.write(configfile)




def save_label_7():
   config = ConfigParser()
   config.read(config_file)
   if not config.has_section("Labels"):
       config.add_section("Labels")
   # Save the colors to the configuration file
   config.set("Labels", "Label_7", str(starting_labels[6]))
   with open(config_file, "w") as configfile:
       config.write(configfile)




def save_label_8():
   config = ConfigParser()
   config.read(config_file)
   if not config.has_section("Labels"):
       config.add_section("Labels")
   # Save the colors to the configuration file
   config.set("Labels", "Label_8", str(starting_labels[7]))
   with open(config_file, "w") as configfile:
       config.write(configfile)




def update_labels():
   global ul_window  # Declare the settings window as a global variable


   # Check if the settings window is already open, and focus on it if it is
   if ul_window is not None and ul_window.winfo_exists():
       ul_window.lift()
       return


   def update_all_labels():
       starting_labels[0] = ul_entry_1.get()
       label_1.configure(text=starting_labels[0])
       starting_labels[1] = ul_entry_2.get()
       label_2.configure(text=starting_labels[1])
       starting_labels[2] = ul_entry_3.get()
       label_3.configure(text=starting_labels[2])
       starting_labels[3] = ul_entry_4.get()
       label_4.configure(text=starting_labels[3])
       starting_labels[4] = ul_entry_5.get()
       label_5.configure(text=starting_labels[4])
       starting_labels[5] = ul_entry_6.get()
       label_6.configure(text=starting_labels[5])
       starting_labels[6] = ul_entry_7.get()
       label_7.configure(text=starting_labels[6])
       starting_labels[7] = ul_entry_8.get()
       label_8.configure(text=starting_labels[7])
       save_all_labels()


   def update_label_1():
       starting_labels[0] = ul_entry_1.get()
       label_1.configure(text=starting_labels[0])
       save_label_1()


   def update_label_2():
       starting_labels[1] = ul_entry_2.get()
       label_2.configure(text=starting_labels[1])
       save_label_2()


   def update_label_3():
       starting_labels[2] = ul_entry_3.get()
       label_3.configure(text=starting_labels[2])
       save_label_3()


   def update_label_4():
       starting_labels[3] = ul_entry_4.get()
       label_4.configure(text=starting_labels[3])
       save_label_4()


   def update_label_5():
       starting_labels[4] = ul_entry_5.get()
       label_5.configure(text=starting_labels[4])
       save_label_5()


   def update_label_6():
       starting_labels[5] = ul_entry_6.get()
       label_6.configure(text=starting_labels[5])
       save_label_6()


   def update_label_7():
       starting_labels[6] = ul_entry_7.get()
       label_7.configure(text=starting_labels[6])
       save_label_7()


   def update_label_8():
       label_8.configure(text=starting_labels[7])
       save_label_8()


   ul_window = CTk.CTkToplevel()
   ul_window.title("Update Labels")
   ul_window.geometry("235x250+" + str(screen_width - 477) + "+340")
   ul_window.iconbitmap("MainLogo.ico")


   ul_entry_1 = CTk.CTkEntry(ul_window)
   ul_entry_1.insert(0, starting_labels[0])
   ul_entry_2 = CTk.CTkEntry(ul_window)
   ul_entry_2.insert(0, starting_labels[1])
   ul_entry_3 = CTk.CTkEntry(ul_window)
   ul_entry_3.insert(0, starting_labels[2])
   ul_entry_4 = CTk.CTkEntry(ul_window)
   ul_entry_4.insert(0, starting_labels[3])
   ul_entry_5 = CTk.CTkEntry(ul_window)
   ul_entry_5.insert(0, starting_labels[4])
   ul_entry_6 = CTk.CTkEntry(ul_window)
   ul_entry_6.insert(0, starting_labels[5])
   ul_entry_7 = CTk.CTkEntry(ul_window)
   ul_entry_7.insert(0, starting_labels[6])
   ul_entry_8 = CTk.CTkEntry(ul_window)
   ul_entry_8.insert(0, starting_labels[7])


   ul_button_1 = CTk.CTkButton(ul_window, text="Update Label", width=20, command=update_label_1)
   ul_button_2 = CTk.CTkButton(ul_window, text="Update Label", width=20, command=update_label_2)
   ul_button_3 = CTk.CTkButton(ul_window, text="Update Label", width=20, command=update_label_3)
   ul_button_4 = CTk.CTkButton(ul_window, text="Update Label", width=20, command=update_label_4)
   ul_button_5 = CTk.CTkButton(ul_window, text="Update Label", width=20, command=update_label_5)
   ul_button_6 = CTk.CTkButton(ul_window, text="Update Label", width=20, command=update_label_6)
   ul_button_7 = CTk.CTkButton(ul_window, text="Update Label", width=20, command=update_label_7)
   ul_button_8 = CTk.CTkButton(ul_window, text="Update Label", width=20, command=update_label_8)


   ul_button_9 = CTk.CTkButton(ul_window, text="Update All", width=20, command=update_all_labels)


   ul_entry_1.grid(column=1, row=0)
   ul_entry_2.grid(column=1, row=1)
   ul_entry_3.grid(column=1, row=2)
   ul_entry_4.grid(column=1, row=3)
   ul_entry_5.grid(column=1, row=4)
   ul_entry_6.grid(column=1, row=5)
   ul_entry_7.grid(column=1, row=6)
   ul_entry_8.grid(column=1, row=7)


   ul_button_1.grid(column=2, row=0)
   ul_button_2.grid(column=2, row=1)
   ul_button_3.grid(column=2, row=2)
   ul_button_4.grid(column=2, row=3)
   ul_button_5.grid(column=2, row=4)
   ul_button_6.grid(column=2, row=5)
   ul_button_7.grid(column=2, row=6)
   ul_button_8.grid(column=2, row=7)


   ul_button_9.grid(column=1, row=8)


   ul_window.mainloop()




def settings():
   global settings_window  # Declare the settings window as a global variable


   # Check if the settings window is already open, and focus on it if it is
   if settings_window is not None and settings_window.winfo_exists():
       settings_window.lift()
       return


   settings_window = CTk.CTkToplevel()
   settings_window.title("Settings")
   settings_window.geometry("220x115+" + str(screen_width - 477) + "+190")
   settings_window.maxsize(width=220, height=115)
   settings_window.minsize(width=220, height=115)
   settings_window.iconbitmap("MainLogo.ico")
   # Instance
   update_labels_btn = CTk.CTkButton(settings_window, text="Update Labels", command=update_labels)
   fg_color_btn = CTk.CTkButton(settings_window, text="Foreground Color", command=fg_color)
   text_color_btn = CTk.CTkButton(settings_window, text="Text Color", command=text_color)


   # Display
   update_labels_btn.pack(pady=5)
   fg_color_btn.pack(pady=5)
   text_color_btn.pack(pady=5)
   settings_window.mainloop()




load_colors_from_config()
load_labels_from_config()


# Main Window -------------------------------------------------------------------------------------
window = CTk.CTk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("Ticket Note Pro")
window.geometry("467x157+" + str(screen_width - 477) + "+0")
window.maxsize(width=467, height=157)
window.minsize(width=467, height=157)
window.iconbitmap("MainLogo.ico")
window.configure(background_color=background_color)


# Instancing --------------------------------------------------------------------------------------
# Frames ------------------------------------------------------------------------------------------
top_left = CTk.CTkFrame(window, fg_color=foreground_color, width=200, height=90)
top_right = CTk.CTkFrame(window, fg_color=foreground_color, width=266, height=90)
bottom = CTk.CTkFrame(window, fg_color=foreground_color, width=468, height=67)
# Top Left Widgets --------------------------------------------------------------------------------
label_1 = CTk.CTkLabel(top_left, text=starting_labels[0], text_color=text_color_change)
label_2 = CTk.CTkLabel(top_left, text=starting_labels[1], text_color=text_color_change)
label_3 = CTk.CTkLabel(top_left, text=starting_labels[2], text_color=text_color_change)
label_4 = CTk.CTkLabel(top_left, text=starting_labels[3], text_color=text_color_change)


entry_1 = CTk.CTkEntry(top_left, width=117, height=20)
entry_2 = CTk.CTkEntry(top_left, width=117, height=20)
entry_3 = CTk.CTkEntry(top_left, width=117, height=20)
entry_4 = CTk.CTkEntry(top_left, width=117, height=20)


copy_button_1 = CTk.CTkButton(top_left, text="Copy", width=10, height=20, command=copy_name)
copy_button_2 = CTk.CTkButton(top_left, text="Copy", width=10, height=20, command=copy_mls)
copy_button_3 = CTk.CTkButton(top_left, text="Copy", width=10, height=20, command=copy_agent)
copy_button_4 = CTk.CTkButton(top_left, text="Copy", width=10, height=20, command=copy_off)


# Top Right Widgets ------------------------------------------------------------------------------
label_5 = CTk.CTkLabel(top_right, text=starting_labels[4], text_color=text_color_change)
label_6 = CTk.CTkLabel(top_right, text=starting_labels[5], text_color=text_color_change)
label_7 = CTk.CTkLabel(top_right, text=starting_labels[6], text_color=text_color_change)
label_8 = CTk.CTkLabel(top_right, text=starting_labels[7], text_color=text_color_change)


entry_5 = CTk.CTkEntry(top_right, width=180, height=20)
entry_6 = CTk.CTkEntry(top_right, width=180, height=20)
entry_7 = CTk.CTkEntry(top_right, width=180, height=20)
entry_8 = CTk.CTkEntry(top_right, width=180, height=20)


copy_button_5 = CTk.CTkButton(top_right, text="Copy", width=10, height=20, command=copy_email)
copy_button_6 = CTk.CTkButton(top_right, text="Copy", width=10, height=20, command=copy_add)
copy_button_7 = CTk.CTkButton(top_right, text="Copy", width=10, height=20, command=copy_issue)
copy_button_8 = CTk.CTkButton(top_right, text="Copy", width=10, height=20, command=copy_category)


# Bottom Widgets ---------------------------------------------------------------------------------
entry_9 = CTk.CTkEntry(bottom, width=156, height=20)
entry_10 = CTk.CTkEntry(bottom, width=222, height=20)
entry_11 = CTk.CTkEntry(bottom, width=156, height=20)
entry_12 = CTk.CTkEntry(bottom, width=222, height=20)


button_9 = CTk.CTkButton(bottom, text="Copy", width=10, height=20, command=copy_entry_9)
button_10 = CTk.CTkButton(bottom, text="Copy", width=10, height=20, command=copy_entry_10)
button_11 = CTk.CTkButton(bottom, text="Copy", width=10, height=20, command=copy_entry_11)
button_12 = CTk.CTkButton(bottom, text="Copy", width=10, height=20, command=copy_entry_12)


copy_template = CTk.CTkButton(bottom, text="Copy Template", width=10, height=20, command=copy_template)
clear_top = CTk.CTkButton(bottom, text="Clear Top", width=10, height=20, command=clear_top, hover_color="red")
clear_bottom = CTk.CTkButton(bottom, text="Clear Bottom", width=10, height=20, command=clear_bottom, hover_color="red")
clear_all = CTk.CTkButton(bottom, text="Clear All", width=10, height=20, command=clear_all, hover_color="red")
settings = CTk.CTkButton(bottom, text="Settings", height=20, width=10, command=settings)


# Placing ----------------------------------------------------------------------------------------
# Frames -----------------------------------------------------------------------------------------
top_left.place(x=0, y=0)
top_right.place(x=202, y=0)
bottom.place(x=0, y=92)


# Top Left Widgets -------------------------------------------------------------------------------
label_1.place(x=0, y=0)
label_2.place(x=0, y=23)
label_3.place(x=0, y=45)
label_4.place(x=0, y=67)


entry_1.place(x=40, y=1)
entry_2.place(x=40, y=23)
entry_3.place(x=40, y=45)
entry_4.place(x=40, y=67)


copy_button_1.place(x=156, y=1)
copy_button_2.place(x=156, y=23)
copy_button_3.place(x=156, y=45)
copy_button_4.place(x=156, y=67)


# Top Right Widgets ------------------------------------------------------------------------------
label_5.place(x=3, y=0)
label_6.place(x=3, y=23)
label_7.place(x=3, y=45)
label_8.place(x=3, y=67)


entry_5.place(x=42, y=1)
entry_6.place(x=42, y=23)
entry_7.place(x=42, y=45)
entry_8.place(x=42, y=67)


copy_button_5.place(x=222, y=1)
copy_button_6.place(x=222, y=23)
copy_button_7.place(x=222, y=45)
copy_button_8.place(x=222, y=67)


# Bottom Widgets ---------------------------------------------------------------------------------
entry_9.place(x=0, y=0)
entry_10.place(x=201, y=0)
entry_11.place(x=0, y=22)
entry_12.place(x=201, y=22)


button_9.place(x=156, y=0)
button_10.place(x=423, y=0)
button_11.place(x=156, y=22)
button_12.place(x=423, y=22)


copy_template.place(x=147, y=45)
clear_top.place(x=247, y=45)
clear_bottom.place(x=317, y=45)
clear_all.place(x=405, y=45)
settings.place(x=0, y=45)


# Calling Window --------------------------------------------------------------------------------
window.mainloop()
