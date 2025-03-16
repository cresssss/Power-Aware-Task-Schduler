import psutil
import time

def get_cpu_usage():
    """Returns the current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def monitor_cpu(low_threshold, high_threshold, callback_low, callback_high, running_flag):
    """
    Continuously monitors CPU usage and triggers appropriate callbacks
    when thresholds are crossed.
    
    :param low_threshold: CPU usage percentage to activate low power mode.
    :param high_threshold: CPU usage percentage to activate high performance mode.
    :param callback_low: Function to call when CPU usage is below the low threshold.
    :param callback_high: Function to call when CPU usage is above the high threshold.
    :param running_flag: Boolean flag to control monitoring loop.
    """
    while running_flag.is_set():
        cpu_usage = get_cpu_usage()
        
        if cpu_usage < low_threshold:
            callback_low()
        elif cpu_usage > high_threshold:
            callback_high()
        
        time.sleep(2)  # Adjust interval as needed