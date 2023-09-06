import datetime
import calendar
from datetime import date

def day_is_sun_thu():
    pass

def day_is_fri():
    pass

def day_is_sat():
    pass

# get today's date
d = date.today()
print('Date is:', d)

# get day name in english
x = calendar.day_name[d.weekday()]
print('Weekday name is:', x)

# Get the current time
now = datetime.datetime.now().time()
print('Current time is:', now)

#Put the correct opening and closing time for the day
gym_break = False
if x == 'Sunday' or x == 'Monday' or x == 'Tuesday' or x == 'Wednesday' or x == 'Thursday':
    # Set the gym's opening and closing times Sunday - Thursday
    gym_open_time = datetime.time(6, 0)  # 6:00 AM
    gym_close_time = datetime.time(23, 0)  # 11:00 PM

    # Check if the gym is in break time
    break_time_start = datetime.time(13, 0)  # 1:00 PM
    break_time_finish = datetime.time(16, 0)  # 4:00 PM
    if break_time_start <= now < break_time_finish:
        gym_break = True

elif x == 'Friday':
    # Set the gym's opening and closing times Friday
    gym_open_time = datetime.time(6, 30)  # 6:30 AM
    gym_close_time = datetime.time(18, 0)  # 6:00 PM

else:
    # Set the gym's opening and closing times Saturday
    gym_open_time = datetime.time(10, 0)  # 10:00 AM
    gym_close_time = datetime.time(23, 0)  # 11:00 PM

# Check if the gym is currently open or closed
if gym_open_time <= now < gym_close_time and not gym_break:
    print("The gym is currently open!")
else:
    if gym_break:
        print(f"Sorry, the gym is in break until: {break_time_finish}")
    else:
        print("Sorry, the gym is currently closed.")

# Calculate how long until the gym closes
if now < gym_open_time:
    time_until_open = datetime.datetime.combine(datetime.date.today(), gym_open_time) - datetime.datetime.now()
    print(f"The gym will be open in {time_until_open.seconds // 3600} hours and {(time_until_open.seconds % 3600) // 60} minutes. at: {gym_open_time}")
elif now > gym_close_time:
    print('The gym will be open tomorrow!')
else:
    time_until_close = datetime.datetime.combine(datetime.date.today(), gym_close_time) - datetime.datetime.now()
    print(f"The gym will be closed in {time_until_close.seconds // 3600} hours and {(time_until_close.seconds % 3600) // 60} minutes. at: {gym_close_time}")
