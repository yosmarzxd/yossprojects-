import os
import time

def update_repositories():
    os.system('sudo apt update && sudo apt upgrade -y')

while True:
    update_repositories()
    time.sleep(42 * 3600)