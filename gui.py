import tkinter as tk
from tkinter import messagebox
import psutil
import threading
import time
import platform
import subprocess

# OS-specific power commands
OS_TYPE = platform.system()

class PowerAwareScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Power-Aware Task Scheduler")
        self.root.geometry("400x300")
        
        # CPU Usage Display
        self.cpu_label = tk.Label(root, text="Current CPU Usage: --%", font=("Arial", 12))
        self.cpu_label.pack(pady=10)
        
        # Low Power Threshold
        self.low_power_label = tk.Label(root, text="Low Power Mode Threshold (%):")
        self.low_power_label.pack()
        self.low_power_entry = tk.Entry(root)
        self.low_power_entry.pack()
        self.low_power_entry.insert(0, "10")
        
        # High Performance Threshold
        self.high_performance_label = tk.Label(root, text="High Performance Mode Threshold (%):")
        self.high_performance_label.pack()
        self.high_performance_entry = tk.Entry(root)
        self.high_performance_entry.pack()
        self.high_performance_entry.insert(0, "50")
        
        # Buttons
        self.start_button = tk.Button(root, text="Start Scheduler", command=self.start_scheduler)
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop Scheduler", command=self.stop_scheduler, state=tk.DISABLED)
        self.stop_button.pack()
        
        self.status_label = tk.Label(root, text="Status: Idle", font=("Arial", 10))
        self.status_label.pack(pady=10)
        
        self.running = False
        
    def start_scheduler(self):
        print("Scheduler Started!")  # Debugging line
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Running")

        # Directly start CPU monitoring
        self.monitor_cpu()

        
    def stop_scheduler(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Stopped")
        
    def monitor_cpu(self):
        """Monitors CPU usage and updates UI every 2 seconds without blocking the event loop."""
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")  # Debugging
        
        # Update the GUI label with the latest CPU usage
        self.cpu_label.config(text=f"Current CPU Usage: {cpu_usage}%")
        
        low_threshold = int(self.low_power_entry.get())
        high_threshold = int(self.high_performance_entry.get())

        # Check CPU thresholds and adjust power mode
        if cpu_usage < low_threshold:
            print("Activating Low Power Mode")  # Debugging
            self.set_low_power_mode()
        elif cpu_usage > high_threshold:
            print("Activating High Performance Mode")  # Debugging
            self.set_high_performance_mode()

        # Schedule the function to run again in 2 seconds
        if self.running:
            self.root.after(2000, self.monitor_cpu)  # Run monitor_cpu() again after 2 seconds



        
    def set_low_power_mode(self):
        if OS_TYPE == "Windows":
            subprocess.run(["powercfg", "/change", "monitor-timeout-ac", "5"])
        elif OS_TYPE == "Linux":
            subprocess.run(["cpufreq-set", "-c", "0", "-g", "powersave"])
        elif OS_TYPE == "Darwin":
            subprocess.run(["pmset", "-a", "reduce", "1"])
        self.status_label.config(text="Status: Low Power Mode Activated")
        
    def set_high_performance_mode(self):
        if OS_TYPE == "Windows":
            subprocess.run(["powercfg", "/change", "monitor-timeout-ac", "15"])
        elif OS_TYPE == "Linux":
            subprocess.run(["cpufreq-set", "-c", "0", "-g", "performance"])
        elif OS_TYPE == "Darwin":
            subprocess.run(["pmset", "-a", "reduce", "0"])
        self.status_label.config(text="Status: High Performance Mode Activated")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PowerAwareScheduler(root)
    root.mainloop()
