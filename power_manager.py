import platform
import subprocess

# Detect the OS\NOS_TYPE = platform.system()
OS_TYPE = platform.system()
def set_low_power_mode():
    """Activates low power mode based on the operating system."""
    if OS_TYPE == "Windows":
        subprocess.run(["powercfg", "/change", "monitor-timeout-ac", "5"], shell=True)
    elif OS_TYPE == "Linux":
        subprocess.run(["cpufreq-set", "-c", "0", "-g", "powersave"], shell=True)
    elif OS_TYPE == "Darwin":  # macOS
        subprocess.run(["pmset", "-a", "reduce", "1"], shell=True)
    print("Switched to Low Power Mode")

def set_high_performance_mode():
    """Activates high performance mode based on the operating system."""
    if OS_TYPE == "Windows":
        subprocess.run(["powercfg", "/change", "monitor-timeout-ac", "15"], shell=True)
    elif OS_TYPE == "Linux":
        subprocess.run(["cpufreq-set", "-c", "0", "-g", "performance"], shell=True)
    elif OS_TYPE == "Darwin":  # macOS
        subprocess.run(["pmset", "-a", "reduce", "0"], shell=True)
    print("Switched to High Performance Mode")