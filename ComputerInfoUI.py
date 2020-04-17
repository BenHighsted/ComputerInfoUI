"""

ComputerInfoUI project. Plan is to make a interface where I can display all the information about my CPU/GPU.
By Ben Highsted. Started April 15th 2020.

"""

import psutil
import platform
import os

import time
import string

#At the moment just want to get all the data working in a terminal app, then convert it into a UI.

def run():
    print("Running...\n")
    calculate_cpu_usage()
    calculate_memory_usage()

    print()

    print("Processor Type:", platform.processor())

    i = 0
    while True:
        calculate_memory_usage()
        calculate_cpu_usage()
        time.sleep(5)
        #below will stop the code. Once the GUI is developed it should run without stopping (unless told to by the user)
        if i == 10:
            break
        i += 1
        

def calculate_memory_usage():
    memory = psutil.virtual_memory() #becomes an array containing memory information
    print("Memory Usage: " + str(memory[2]) + "%")

def calculate_cpu_usage():
    process = psutil.Process(os.getpid())
    print(process.cpu_percent())

run()