
# Main Program

import time
import fetch_time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("Current Time: ", current_time)
print('''
        ----------------------------------
              CITY      | TIME DIFFERENCE
        ----------------------------------
        1. New York     |  -  10:30
        2. Sydney       |  +  5:30
        3. Johannesburg |  -  3:30
        4. EXIT
        ----------------------------------
        ''')
while True:

    ch = int(input("\nEnter choice: "))
    if ch == 1:
        print("---------------------")
        print("NEW YORK TIME :")
        fetch_time.newyork_time(current_time)
        print("---------------------")
    elif ch == 2:
        print("---------------------")
        print("SYDNEY TIME :")
        fetch_time.sydney_time(current_time)
        print("---------------------")
    elif ch == 3:
        print("---------------------")
        print("JOHANNESBURG TIME :")
        fetch_time.Johannesburg_time(current_time)
        print("---------------------")
    elif ch == 4:
        break
    else:
        print("Wrong choice!!!")

################################################################################


