import threading
import tkinter as tk
from gui import PowerAwareScheduler
from cpu_monitor import monitor_cpu
from power_manager import set_low_power_mode, set_high_performance_mode

def start_scheduler(app, running_flag):
    """Starts the CPU monitoring thread."""
    running_flag.set()
    low_threshold = int(app.low_power_entry.get())
    high_threshold = int(app.high_performance_entry.get())
    
    monitor_thread = threading.Thread(
        target=monitor_cpu, 
        args=(low_threshold, high_threshold, set_low_power_mode, set_high_performance_mode, running_flag),
        daemon=True
    )
    monitor_thread.start()

def stop_scheduler(running_flag):
    """Stops the CPU monitoring thread."""
    running_flag.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = PowerAwareScheduler(root)
    
    running_flag = threading.Event()
    
    app.start_button.config(command=lambda: start_scheduler(app, running_flag))
    app.stop_button.config(command=lambda: stop_scheduler(running_flag))
    
    root.mainloop()