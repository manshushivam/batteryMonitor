import tkinter as tk
from .battery_info import get_battery_info
from .notifications import notify_battery_full
import time

def format_time(seconds):
    # Format seconds into hours, minutes, seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f"{h}h {m}m {s}s"
    
def update_battery_info(root, battery_label, plugged_label, time_label):
    info = get_battery_info()
    battery_label.config(text=f"Battery: {info['percent']}%", font=("Helvetica", 20))  # Increase font size
    plugged_label.config(text=f"Plugged In: {info['plugged']}", font=("Helvetica", 16))  # Increase font size
    if info['plugged']:
        time_label.config(text=f"Plugged in for: {format_time(info['secsleft'])}", font=("Helvetica", 12))  # Increase font size
    else:
        time_label.config(text="", font=("Helvetica", 12))  # Increase font size
    if info['percent'] == 100 and info['plugged']:
        notify_battery_full()
    root.after(10000, update_battery_info, root, battery_label, plugged_label, time_label)  # update every 10 seconds

    

    
def create_gui():
    root = tk.Tk()
    root.title("Battery Monitor")
    root.geometry("400x300")  # width x height

    battery_label = tk.Label(root, text="Battery: ")
    battery_label.pack(anchor='center')


    plugged_label = tk.Label(root, text="Plugged In: ")
    plugged_label.pack()

    time_label = tk.Label(root, text="")
    time_label.pack()
    

    
    update_battery_info(root, battery_label, plugged_label, time_label)
    


    root.mainloop()
