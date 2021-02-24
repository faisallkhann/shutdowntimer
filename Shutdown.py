import os

def sd():
    time_min = input("After how many minutes do you want to shutdown your PC? : ")
    
    time_min = int(time_min)
    time_sec = time_min * 60

    confirm = input(f"Your PC will shut down in {time_min} minutes. Are you sure? (Enter y to confirm): ")

    if confirm == "y":
        shutdown = os.system(f"shutdown -s -t {time_sec}")
        shutdown        
    else:
            quit()
    quit()
def abort():
    abrt = input("Do You Want To Abort The Schedulled Shutdown? (Enter y to confirm): ")
    if abrt == "y":
        a = os.system("shutdown -a")
    else:
        quit()
    quit()

print('''


███████ ██   ██ ██    ██ ████████ ██████   ██████  ██     ██ ███    ██     ████████ ██ ███    ███ ███████ ██████  
██      ██   ██ ██    ██    ██    ██   ██ ██    ██ ██     ██ ████   ██        ██    ██ ████  ████ ██      ██   ██ 
███████ ███████ ██    ██    ██    ██   ██ ██    ██ ██  █  ██ ██ ██  ██        ██    ██ ██ ████ ██ █████   ██████  
     ██ ██   ██ ██    ██    ██    ██   ██ ██    ██ ██ ███ ██ ██  ██ ██        ██    ██ ██  ██  ██ ██      ██   ██ 
███████ ██   ██  ██████     ██    ██████   ██████   ███ ███  ██   ████        ██    ██ ██      ██ ███████ ██   ██ 
                                                                                              v1.0 by Faisal Khan
                                                                                                         
    
    [1] Set the Shutdown Timer
    [2] Abort the last scheduled shutdown
    [3] Enter Q to Quit
  
   ''') 


while True:

    while True:

        input_first = input("Enter your choice: ")
        try:
            input_first = int(input_first)
            break
        except:
            if input_first == "q":
                print("Exiting!!!")
                quit()
            else:
                print("Bad Input!!! Try again or enter Q to quit.")
            continue
    if input_first == 1:
        sd()
        continue
    if input_first == 2:
        abort()
        continue
    if input_first == 3:
        print("Exiting!!!")
        quit()
    break
quit()