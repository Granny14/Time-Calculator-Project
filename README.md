# Time Calculator

# Description
- **The Time Calculator is a Python function that adds a duration to a given start time, accounting for the change in AM/PM, and optionally the day of the week. The function also calculates the number of days later if the result extends into the next day or further.**

# Features

- **Adds hours and minutes to a given start time.**
- **Adjusts the time for AM/PM accordingly.**
- **Handles overflow into the next day(s).**
- **Optionally returns the day of the week if provided.**
- **Provides the number of days later if the result extends beyond the current day.**

# Function Signature
    # Function implementation
def add_time(start, duration, starting_day=None):
  
# Parameters
- **start: A string representing the start time in the format HH:MM AM/PM (e.g., "3:00 PM").**
- **duration: A string representing the duration time in the format HH:MM (e.g., "3:10").**
- **starting_day: (Optional) A string representing the starting day of the week (e.g., "Monday").**

# Returns
- **A string with the new time, adjusted for AM/PM, and the number of days later if applicable.**

# Example usages
- **print(add_time('3:00 PM', '3:10'))  # Returns: 6:10 PM**
- **print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday**
- **print(add_time('11:43 AM', '00:20'))  # Returns: 12:03 PM**
- **print(add_time('10:10 PM', '3:30'))  # Returns: 1:40 AM (next day)**
- **print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)**
- **print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)**

# Installation
- **To use this function, clone the repository and import the function into your Python script.**

- **git clone [https://github.com/your-username/time-calculator.git](https://github.com/Granny14/Time-Calculator-Project.git)**

# Running the Tests
- **You can run the provided test cases to verify the functionality of the add_time function.**

# Include your test cases here to verify the functionality

# Contributing
- **Contributions are welcome! If you have suggestions for improvements or new features, please submit an issue or a pull request.**

# License
- **This project is licensed under the MIT License - see the LICENSE file for details.**
