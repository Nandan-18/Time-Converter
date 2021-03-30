# Program 13
"""Taking the current time in India calculate the time in
        a. New York (10 hours 30 minutes behind Calcutta)
        b. Sydney(5 hours 30 minutes ahead of Calcutta)
        c. Johannesburg ( 3 hours 30 minutes behind Calcutta)
       Display the time in 24 hours format."""

# Main Program:

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

# OUTPUT #
''' Current Time:  20:29:19

        ----------------------------------
              CITY      | TIME DIFFERENCE
        ----------------------------------
        1. New York     |  -  10:30
        2. Sydney       |  +  5:30
        3. Johannesburg |  -  3:30
        4. EXIT
        ----------------------------------
        

Enter choice: 1
---------------------
NEW YORK TIME :
09:59:19
---------------------

Enter choice: 2
---------------------
SYDNEY TIME :
01:59:19
---------------------

Enter choice: 3
---------------------
JOHANNESBURG TIME :
16:59:19
---------------------

Enter choice: 4
>>> '''
