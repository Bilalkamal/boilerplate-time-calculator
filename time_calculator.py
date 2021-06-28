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
def convert_hrs_to24(hours):
    if hours == 12:
        return 12
    else: return 12 + hours 
def convert_to_12(hours):
    if hours == 24:
        return 0
    else: return 12 - hours


def add_time(start, duration, day = None):
    if day: day = day.title()
    print(f'day is: {day}')
    minutes_counter,new_hours,hours_counter = 0,0,0
    start_hours ,start_minutes, start_am_pm = get_hours_min(start)
    duration_hours, duration_minutes = get_hours_min(duration)
    minutes_counter += start_minutes +duration_minutes
    if minutes_counter >=60: new_hours, minutes_counter = convert_min_to_hrs(minutes_counter)
    if start_am_pm == "PM": hours_counter , start_hours = convert_hrs_to24(start_hours), 0 
    hours_counter += new_hours + duration_hours + start_hours
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    if minutes_counter <10: minutes_counter = f"0{minutes_counter}"
    time = hours_counter%12
    if time == 0: time = 12
    if hours_counter <11 and day is None: return f'{time}:{minutes_counter} AM'
    if hours_counter <24 and day is None and hours_counter >11: return f'{time}:{minutes_counter} PM'
    if hours_counter <11 and day is not None: return f'{time}:{minutes_counter} AM, {day.title()}'
    if hours_counter <24 and day is not None and hours_counter >11: return f'{time}:{minutes_counter} PM, {day.title()}'
    time = hours_counter%24
    if time == 0: time = 12
    days_past = hours_counter // 24
    if hours_counter >= 24 and day is None:
        if hours_counter // 24 == 1:
            am_time = True
            if hours_counter // 24 > 11: hours, am_time = convert_to_12(hours_counter//24), False
            if am_time:return f'{time}:{minutes_counter} AM (next day)'
            if not am_time: return f'{hours}:{minutes_counter} PM (next day)'
        else:
            am_time = True
            if hours_counter // 24 > 11: hours, am_time = convert_to_12(hours_counter%24), False
            if am_time:return f'{time}:{minutes_counter} PM ({days_past} days later)'
            if not am_time: return f'{hours}:{minutes_counter} AM ({days_past} days later)'
    if hours_counter >= 24 and day is not None:
        day_index = days.index(day) + days_past%7
        if day_index ==7 :day_index =0
        am_time = True
        if hours_counter // 24 == 1:
            if hours_counter // 24 > 11: hours, am_time = convert_to_12(hours_counter//24), False
            if am_time:return f'{time}:{minutes_counter} AM, {days[day_index]} (next day)'
            if not am_time: return f'{hours}:{minutes_counter} PM, {days[day_index]} (next day)'
        else:
            days_past = hours_counter // 24
            if hours_counter // 24 > 11: hours, am_time = convert_to_12(hours_counter%24), False
            if am_time:return f'{time}:{minutes_counter} PM, {days[day_index]} ({days_past} days later)'
            if not am_time: return f'{hours}:{minutes_counter} AM, {days[day_index]} ({hours_counter // 24} days later)'

    # return new_time
print(add_time("8:16 PM", "466:02"))
# print(add_time("11:30 AM", "2:32", "Monday"))
# print(add_time("11:43 AM", "00:20"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("11:43 PM", "24:20", "tueSday"))
# print(add_time("6:30 PM", "205:12"))