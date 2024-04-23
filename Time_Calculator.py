def add_time(start, duration, starting_day=""):
    #split the start
    start_time = start.split()
    end = start_time[1]
    start_time = start_time[0].split(":")

    #24 hours time format
    if end == "PM":
        start_time[0] = int(start_time[0]) + 12

    #split the duration
    dur_time = duration.split(":")

    #add hours and minute

    new_minute = int(start_time[1]) + int(dur_time[1])
    new_hours = int(start_time[0]) + int(dur_time[0])
    if new_minute >= 60:
        add_hours = new_minute // 60
        new_minute = new_minute % 60
        new_hours += add_hours

    #calculate the add_days
    add_days = 0
    if new_hours > 24:
        add_days = new_hours // 24
        new_hours = new_hours % 24

    #calculate the AM and PM

    if new_hours > 0 and new_hours < 12:
        end = "AM"
    elif new_hours > 12:
        end = "PM"
        new_hours -= 12
    elif new_hours == 12:
        end = "PM"
    else:   # for 0
        new_hours += 12;
        end = "AM"
    
    #for days > 0
    days_later = ""
    if add_days > 0:
        if add_days == 1:
            days_later = " (next day)"
        else:
            days_later = " (" + str(add_days) + " days later)"

    weeks_days =("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

    # for starting day is given
    if starting_day:
        day_index = 0
        weeks = add_days // 7
        i = weeks_days.index(starting_day.lower().capitalize()) + (add_days - 7 * weeks)
        if i > 6 :
            i -= 7
        day = ", " + weeks_days[i]
    else:
        day = ""
    
    #merge into new_time
    new_time = str(new_hours) + ":" + \
     f"{str(new_minute):>02}" + \
     " " + end + day + days_later
    return new_time

print(add_time("10:10 PM","3:30"))