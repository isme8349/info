import tkinter as tk
from tkinter import ttk
import platform
import psutil

def get_system_info():
    system_info = {
        'Operating System': platform.system(),
        'OS Version': platform.version(),
        'Architecture': platform.architecture(),
        'Processor': platform.processor(),
        'CPU Cores': psutil.cpu_count(logical=False),
        'Logical Processors': psutil.cpu_count(logical=True),
        'RAM Size (GB)': round(psutil.virtual_memory().total / (1024 ** 3), 2),
        'Disk Size (GB)': round(psutil.disk_usage('/').total / (1024 ** 3), 2),
    }
    return system_info

def display_info(language):
    info = get_system_info()
    text_output.delete(1.0, tk.END)  # Clear previous text
    if language == 'fa':
        text_output.insert(tk.END, "اطلاعات سیستم:\n")
    else:
        text_output.insert(tk.END, "System Information:\n")
    
    for key, value in info.items():
        text_output.insert(tk.END, f"{key}: {value}\n")

def change_language(lang):
    display_info(lang)

def exit_program():
    root.quit()  


root = tk.Tk()
root.title("System Information")


lang_frame = ttk.Frame(root)
lang_frame.pack(pady=10)

# Language selection buttons
btn_fa = ttk.Button(lang_frame, text="فارسی", command=lambda: change_language('fa'))
btn_fa.grid(row=0, column=0, padx=5)

btn_en = ttk.Button(lang_frame, text="English", command=lambda: change_language('en'))
btn_en.grid(row=0, column=1, padx=5)


btn_exit = ttk.Button(root, text="Exit", command=exit_program)
btn_exit.pack(pady=10)


text_output = tk.Text(root, width=50, height=15, font=("Helvetica", 12))
text_output.pack(pady=10)


display_info('en')


root.mainloop()
