# Supporting Program
# fetch_time.py

def print_time(hr, mins, sec):
    if mins >= 60:
        min_hr = mins // 60
        mins %= 60
        hr += min_hr
    if hr >= 24:
        hr %= 24
    elif hr <= 0:
        hr = 24 + hr
    sec = int(sec)
    print("%02d:%02d:%02d" % (hr, mins, sec))


# New York    
def newyork_time(current_time):
    hr, mins, sec = current_time.split(':')
    hr = int(hr) - 11
    mins = int(mins) + 30
    print_time(hr, mins, sec)


# Sydney 
def sydney_time(current_time):
    hr, mins, sec = current_time.split(':')
    hr = int(hr) + 5
    mins = int(mins) + 30
    print_time(hr, mins, sec)


# Johannesburg
def Johannesburg_time(current_time):
    hr, mins, sec = current_time.split(':')
    hr = int(hr) - 4
    mins = int(mins) + 30
    print_time(hr, mins, sec)
