def add_time(start, duration, starting_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Split start time into components
    start_parts = start.split()
    start_time = start_parts[0]
    period = start_parts[1]

    # Split start time into hours and minutes
    start_hour, start_minute = map(int, start_time.split(':'))

    # Convert start time to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Split duration time into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate the new minutes and hours
    new_minute = start_minute + duration_minute
    additional_hour = new_minute // 60
    new_minute = new_minute % 60

    new_hour = start_hour + duration_hour + additional_hour
    days_later = new_hour // 24
    new_hour = new_hour % 24

    # Determine the new period and adjust hour to 12-hour format
    if new_hour >= 12:
        period = "PM"
        if new_hour > 12:
            new_hour -= 12
    else:
        period = "AM"
        if new_hour == 0:
            new_hour = 12

    # Format the new time
    new_time = f"{new_hour}:{new_minute:02d} {period}"

    # Add the day of the week if provided
    if starting_day:
        starting_day = starting_day.capitalize()
        start_day_index = days_of_week.index(starting_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Add the number of days later if needed
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

# Testing the function with provided examples
print(add_time('3:00 PM', '3:10'))  # Returns: 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))  # Returns: 12:03 PM
print(add_time('10:10 PM', '3:30'))  # Returns: 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)
