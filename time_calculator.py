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


def add_time(start, duration, day = None):
    minutes_counter,new_hours,hours_counter = 0,0,0
    start_hours ,start_minutes, start_am_pm = get_hours_min(start)
    duration_hours, duration_minutes = get_hours_min(duration)
    minutes_counter += start_minutes +duration_minutes
    if minutes_counter >=60: new_hours, minutes_counter = convert_min_to_hrs(minutes_counter)
    if start_am_pm == "PM": hours_counter , start_hours = convert_hrs_to24(start_hours), 0 
    hours_counter += new_hours + duration_hours + start_hours
    
    print(hours_counter)
    print(minutes_counter)
    if hours_counter <11 and day is None: return f'{hours_counter%12}:{minutes_counter} AM'
    if hours_counter <24 and day is None and hours_counter >11: return f'{hours_counter%12}:{minutes_counter} PM'
    if hours_counter <11 and day is not None: return f'{hours_counter%12}:{minutes_counter} AM, {day.title()}'
    if hours_counter <24 and day is not None and hours_counter >11: return f'{hours_counter%12}:{minutes_counter} PM, {day.title()}'
    
    # return new_time
print(add_time("0:30 AM", "200:12","Monday"))