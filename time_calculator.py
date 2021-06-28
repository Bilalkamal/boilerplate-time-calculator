def get_hours_min(time):
    if "AM" in time or "PM" in time:
        hours, min = int(time.split(":")[0]), int(time.split(":")[1].split()[0])
        am_pm = time.split(":")[1].split()[1]
        return hours, min, am_pm
    return int(time.split(":")[0]), int(time.split(":")[1])
def convert_min_to_hrs(minutes):
    hours = minutes // 60
    rem_minutes = minutes % 60
    return hours, rem_minutes


def add_time(start, duration, day = None):
    if day: day = day.title()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    minutes_counter,min_to_hrs,hours_counter,new_time = 0,0,0,""
    start_hours ,start_minutes, start_am_pm = get_hours_min(start)
    duration_hours, duration_minutes = get_hours_min(duration)
    minutes_counter += start_minutes +duration_minutes
    am = True
    if start_am_pm == "PM" and start_hours < 12: start_hours += 12
    if minutes_counter >=60: min_to_hrs, minutes_counter = convert_min_to_hrs(minutes_counter)
    hours_counter += min_to_hrs + duration_hours + start_hours
    days_later,remaining_time = hours_counter // 24, hours_counter % 24
    if remaining_time > 12: new_time += f"{remaining_time%12}"
    if remaining_time == 12 or remaining_time == 0: new_time += f"12" 
    if remaining_time <12 and remaining_time >0: new_time += f'{remaining_time}'
    if remaining_time >= 12: am = False
    new_time += f':0{minutes_counter}'if minutes_counter <10 else f':{minutes_counter}'
    new_time += f' AM' if am else f' PM'
    if day is not None:
        day_index = days.index(day) + days_later%7
        if day_index == 7: day_index=0
        new_time += f', {days[day_index]}'
    if days_later == 1: new_time += ' (next day)'
    if days_later > 1 : new_time += f' ({days_later} days later)'
    return new_time
    
    
    

    # return new_time
print(add_time("3:30 PM", "2:12", "Monday"))
# print(add_time("11:30 AM", "2:32", "Monday"))
# print(add_time("11:43 AM", "00:20"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("11:43 PM", "24:20", "tueSday"))
# print(add_time("6:30 PM", "205:12"))



