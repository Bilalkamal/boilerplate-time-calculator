def get_hours_min(time):
    if "AM" in time or "PM" in time:
        hours, min = int(time.split(":")[0]), int(time.split(":")[1].split()[0])
        am_pm = time.split(":")[1].split()[1]
        return hours, min, am_pm
    hours, min = int(time.split(":")[0]), int(time.split(":")[1])
    return hours, min
    


def add_time(start, duration):
    minutes_counter = 0
    hours_counter = 0
    start_hours ,start_minutes, start_am_pm = get_hours_min(start)
    duration_hours, duration_minutes = get_hours_min(duration)
    minutes_counter += start_minutes +duration_minutes
    
    print(minutes_counter)



    # return new_time
print(add_time("11:55 PM", "2:45"))