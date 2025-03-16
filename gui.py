import tkinter as tk
from tkinter import messagebox
import psutil
import threading
import time
import platform
import subprocess
import power_manager  # Ensure this is at the top


# OS-specific power commands
OS_TYPE = platform.system()

class PowerAwareScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Power-Aware Task Scheduler")
        self.root.geometry("400x300")
        self.current_mode = "Normal"  # Track current power mode

        
        # CPU Usage Display
        # self.cpu_label = tk.Label(root, text="Current CPU Usage: --%", font=("Arial", 12))
        # self.cpu_label.pack(pady=10)
        self.cpu_usage_label = tk.Label(self.root, text="Current CPU Usage: --%")
        self.cpu_usage_label.pack()

        
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
        """Stops the CPU monitoring and prevents further power state changes."""
        print("Scheduler Stopped!")  # Debugging
        self.running = False  # Set flag to stop monitoring
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Stopped")



        
    def monitor_cpu(self):
        """Continuously monitors CPU usage and adjusts power mode accordingly."""
        cpu_usage = psutil.cpu_percent(interval=1)
        self.cpu_usage_label.config(text=f"Current CPU Usage: {cpu_usage:.1f}%")

        low_threshold = int(self.low_power_entry.get())
        high_threshold = int(self.high_performance_entry.get())


        if cpu_usage < low_threshold and self.current_mode != "Low Power":
            print("Activating Low Power Mode")
            power_manager.set_low_power_mode()
            self.status_label.config(text="Status: Low Power Mode Activated")
            self.current_mode = "Low Power"

        elif cpu_usage > high_threshold and self.current_mode != "High Performance":
            print("Activating High Performance Mode")
            power_manager.set_high_performance_mode()
            self.status_label.config(text="Status: High Performance Mode Activated")
            self.current_mode = "High Performance"

        # Schedule next check
        if self.running:
            self.root.after(3000, self.monitor_cpu)







        
    import subprocess

def set_low_power_mode():
    """Forces CPU into low power mode by limiting CPU processing power."""
    power_scheme = "381b4222-f694-41f0-9685-ff5bb260df2e"  # Balanced Power Scheme
    print(f"Applying Low Power Mode to scheme: {power_scheme}")

    # Force changes
    subprocess.run(["powercfg", "-setacvalueindex", power_scheme, "SUB_PROCESSOR", "PROCTHROTTLEMIN", "5"], shell=True)
    subprocess.run(["powercfg", "-setacvalueindex", power_scheme, "SUB_PROCESSOR", "PROCTHROTTLEMAX", "50"], shell=True)
    subprocess.run(["powercfg", "-setactive", power_scheme], shell=True)

    print("Switched to Low Power Mode")

        
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
