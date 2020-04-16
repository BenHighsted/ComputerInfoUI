"""

ComputerInfoUI project. Plan is to make a interface where I can display all the information about my CPU/GPU.
By Ben Highsted. Started April 15th 2020.

"""

import psutil
import platform
import os

import time

def run():
    print("Running...\n")
    print("CPU Percent:", psutil.cpu_percent())
    print(psutil.virtual_memory())
    memory = psutil.virtual_memory() #becomes an array containing memory information

    print()

    print("Processor Type:", platform.processor())

    i = 0
    while True:
        process = psutil.Process(os.getpid())
        print("Memory Usage: " + str(round(process.memory_percent() * 100, 2)) + "%")
        time.sleep(5)
        if i == 10:
            break
        i += 1
    
"""

For windows https://stackoverflow.com/questions/938733/total-memory-used-by-python-process.
Will need to install WMI on my windows computer.

def memory():
    from wmi import WMI
    w = WMI('.')
    result = w.query("SELECT WorkingSet FROM Win32_PerfRawData_PerfProc_Process WHERE IDProcess=%d" % os.getpid())
    return int(result[0].WorkingSet)

"""

run()