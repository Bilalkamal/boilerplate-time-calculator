def get_hours_min(time):
    if "AM" in time or "PM" in time:
        hours, min = int(time.split(":")[0]), int(time.split(":")[1].split()[0])
        am_pm = time.split(":")[1].split()[1]
        return hours, min, am_pm
    hours, min = int(time.split(":")[0]), int(time.split(":")[1])
    return hours, min
    
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
    minutes_counter,new_hours,hours_counter = 0,0,0
    start_hours ,start_minutes, start_am_pm = get_hours_min(start)
    duration_hours, duration_minutes = get_hours_min(duration)
    minutes_counter += start_minutes +duration_minutes
    if minutes_counter >=60: new_hours, minutes_counter = convert_min_to_hrs(minutes_counter)
    if start_am_pm == "PM": hours_counter , start_hours = convert_hrs_to24(start_hours), 0 
    hours_counter += new_hours + duration_hours + start_hours
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    if hours_counter <11 and day is None: return f'{hours_counter%12}:{minutes_counter} AM'
    if hours_counter <24 and day is None and hours_counter >11: return f'{hours_counter%12}:{minutes_counter} PM'
    if hours_counter <11 and day is not None: return f'{hours_counter%12}:{minutes_counter} AM, {day.title()}'
    if hours_counter <24 and day is not None and hours_counter >11: return f'{hours_counter%12}:{minutes_counter} PM, {day.title()}'
    if hours_counter >= 24 and day is None:
        if hours_counter // 24 == 1:
            am_time = True
            if hours_counter // 24 > 11: hours, am_time = convert_to_12(hours_counter//24), False
            if am_time:return f'{hours_counter%24}:{minutes_counter} AM (next day)'
            if not am_time: return f'{hours}:{minutes_counter} PM (next day)'
        else:
            am_time = True
            days_past = hours_counter // 24
            if hours_counter // 24 > 11: hours, am_time = convert_to_12(hours_counter//24), False
            if am_time:return f'{hours_counter%24}:{minutes_counter} AM ({days_past} days later)'
            if not am_time: return f'{hours}:{minutes_counter} PM ({days_past} days later)'
    if hours_counter >= 24 and day is not None:
        if hours_counter // 24 == 1:
            am_time = True
            if hours_counter // 24 > 11: hours, am_time = convert_to_12(hours_counter//24), False
            if am_time:return f'{hours_counter%24}:{minutes_counter} AM (next day)'
            if not am_time: return f'{hours}:{minutes_counter} PM (next day)'
        else:
            days_past = hours_counter // 24
            am_time = True
            if hours_counter // 24 > 11: hours, am_time = convert_to_12(hours_counter//24), False
            if am_time:return f'{hours_counter%24}:{minutes_counter} AM, {days[days.index(day) + days_past%7]} ({days_past} days later)'
            
            if not am_time: return f'{hours}:{minutes_counter} PM, {days[days.index(day) + days_past%7]} ({hours_counter // 24} day)'

    # return new_time
print(add_time("3:00 PM", "3:10"))