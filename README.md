# Power-Aware-Task-Schduler


# Overview

The Power-Aware Task Scheduler is a Python-based tool designed to dynamically adjust CPU power states based on real-time CPU usage. It provides a graphical user interface (GUI) built with Tkinter, allowing users to set CPU usage thresholds and automate power management. The scheduler helps optimize energy consumption by switching between low power and high-performance modes as needed.

Features

Real-time CPU usage monitoring

User-defined thresholds for low power and high-performance modes

Automatic switching between power states

Cross-platform support (Windows, Linux, macOS)

Start and stop functionality

Installation

Prerequisites

Ensure you have Python installed on your system. The following dependencies are required:

**pip install psutil**

Running the Application

    Clone the repository or download the source code.

    Open a terminal or command prompt in the project directory.

Run the application using:
*Must be run as admin*

**python main.py**

**How It Works**

*Monitoring CPU Usage*

    The scheduler continuously monitors CPU utilization at fixed intervals.

    The CPU percentage is displayed in the GUI and updated every two seconds.

*Switching Power States*

    If CPU usage drops below the Low Power Threshold, the system switches to Low Power Mode to conserve energy.

    If CPU usage rises above the High Performance Threshold, the system switches to High Performance Mode to ensure adequate processing power.

    If CPU usage remains between the two thresholds, the system remains in its current power mode.

*User Interaction*

    Users can manually set their preferred low power and high-performance thresholds.

    The "Start Scheduler" button begins monitoring and power adjustments.

    The "Stop Scheduler" button halts monitoring and prevents further power state changes.

**Platform-Specific Power Adjustments**

The scheduler utilizes OS-specific commands to adjust power settings:

    Windows: powercfg commands are used to modify power plans.

    Linux: cpufreq-set is used to switch between "powersave" and "performance" modes.

    macOS: pmset commands are used to adjust power settings.

**Limitations and Future Improvements**

    Some systems may require administrator privileges to modify power settings.

    Power adjustments may have limited effectiveness on modern systems with built-in power management.

    Future updates could include background execution as a system tray application and logging of power state changes for analysis.

*Why You May Not See a Difference:*
    Laptop Battery Power vs. CPU Scaling

This script does not modify battery settings directly.
    It mainly reduces CPU frequency and power consumption.
    If your system already manages power efficiently, you may not notice a major change.
    Some CPUs Have Locked Power States

    Modern Intel and AMD processors dynamically scale power on their own.
    If your system already does this, manual power control may have limited effect.