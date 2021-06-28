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

def add_time(start, duration):
    minutes_counter = 0
    hours_counter = 0
    start_hours ,start_minutes, start_am_pm = get_hours_min(start)
    duration_hours, duration_minutes = get_hours_min(duration)
    minutes_counter += start_minutes +duration_minutes
    new_hours = 0
    if minutes_counter >=60: new_hours, minutes_counter = convert_min_to_hrs(minutes_counter)
    # print(f'duration {duration_hours}')
    if start_am_pm == "PM": hours_counter  = convert_hrs_to24(start_hours)
    hours_counter += new_hours + duration_hours
    
    print(hours_counter)
    print(minutes_counter)
    # return new_time
print(add_time("3:30 PM", "2:12"))