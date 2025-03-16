import platform
import subprocess

# Detect the OS\NOS_TYPE = platform.system()
OS_TYPE = platform.system()
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




def set_high_performance_mode():
    """Forces CPU into high performance mode by allowing 100% power usage."""
    power_scheme = "381b4222-f694-41f0-9685-ff5bb260df2e"  # Balanced Power Scheme
    print(f"Applying High Performance Mode to scheme: {power_scheme}")

    # Force changes
    subprocess.run(["powercfg", "-setacvalueindex", power_scheme, "SUB_PROCESSOR", "PROCTHROTTLEMIN", "100"], shell=True)
    subprocess.run(["powercfg", "-setacvalueindex", power_scheme, "SUB_PROCESSOR", "PROCTHROTTLEMAX", "100"], shell=True)
    subprocess.run(["powercfg", "-setactive", power_scheme], shell=True)

    print("Switched to High Performance Mode")

