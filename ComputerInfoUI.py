"""

ComputerInfoUI project. Plan is to make a interface where I can display all the information about my CPU/GPU.
By Ben Highsted. Started April 15th 2020.

"""

import psutil

def run():
    print("Running...\n")
    print(psutil.cpu_percent())
    print(psutil.virtual_memory())

run()