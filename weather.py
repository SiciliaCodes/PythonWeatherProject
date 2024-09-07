import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """

    if not isinstance(temp, (int, float)):
        raise TypeError("Temperature must be a numeric value (int or float)")

    return f"{temp}{DEGREE_SYMBOL}" 

pass

def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    try:
        date_obj = datetime.fromisoformat(iso_string)
    except ValueError:
        raise ValueError("Invalid ISO format date string") 

    return date_obj.strftime("%A %d %B %Y")
    
pass



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_celsius = (temp_in_fahrenheit - 32) * 5/9
    return round(temp_in_celsius, 1) 

pass


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    if not weather_data:  # Check if the list is empty
        return None  # Or you could raise an exception here

    total = sum(weather_data)
    mean = total / len(weather_data)
    return mean

pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)   

        for row in reader:
            if row:  # Check if the row is not empty
                data.append(row)
    return data

pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return None

    min_value = weather_data[0]  # Initialize with the first value
    min_index = 0

    for i, value in enumerate(weather_data):
        if value <= min_value:  # Check for less than or equal to find the last occurrence
            min_value = value
            min_index = i

    return min_value, min_index
pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    if not weather_data:
        return None

    max_value = weather_data[0]  # Initialize with the first value
    max_index = 0

    for i, value in enumerate(weather_data):
        if value >= max_value:  # Check for greater than or equal to find the last occurrence
            max_value = value
            max_index = i

    return max_value, max_index
pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "No data available for summary."

    # Extract data for calculations
    dates = [row[0] for row in weather_data]
    min_temps = [float(row[1]) for row in weather_data]
    max_temps = [float(row[2]) for row in weather_data]
    rainfall = [float(row[3]) for row in weather_data]

    # Calculate summary statistics
    start_date = convert_date(min(dates))
    end_date = convert_date(max(dates))
    lowest_temp, lowest_temp_date_index = find_min(min_temps)
    highest_temp, highest_temp_date_index = find_max(max_temps)
    total_rainfall = sum(rainfall)
    average_rainfall = calculate_mean(rainfall)

    # Format the summary
    summary = f"""
    Weather summary for {start_date} to {end_date}:

    - Lowest temperature: {format_temperature(lowest_temp)} on {convert_date(dates[lowest_temp_date_index])}
    - Highest temperature: {format_temperature(highest_temp)} on {convert_date(dates[highest_temp_date_index])}
    - Total rainfall: {total_rainfall:.2f} mm
    - Average daily rainfall: {average_rainfall:.2f} mm
        """

    return summary
pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    if not weather_data:
        return "No data available for daily summary."

    daily_summaries = []
    for day_data in weather_data:
        date = convert_date(day_data[0])
        min_temp = format_temperature(float(day_data[1]))
        max_temp = format_temperature(float(day_data[2]))
        rainfall = float(day_data[3])

        daily_summary = f"""
        --- {date} ---
        Minimum temperature: {min_temp}
        Maximum temperature: {max_temp}
        Rainfall: {rainfall:.2f} mm
        """
        daily_summaries.append(daily_summary)

    return "\n".join(daily_summaries)


pass
