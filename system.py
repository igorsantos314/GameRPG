import os
import subprocess

try:
    subprocess.check_output("apt install nmap", shell=True);

except subprocess.CalledProcessError as e:
    print('Erro id: ',e)
