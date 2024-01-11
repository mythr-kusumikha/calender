from datetime import datetime, timedelta
from collections import defaultdict

def parse_booking_data(data_lines):
    booking_splits = []
    for line in data_lines:
        parts = line.split()
        if len(parts) == 3:
            try:
                timestamp = datetime.strptime(parts[0] + ' ' + parts[1], '%Y-%m-%d %H:%M:%S')
            except ValueError:
                timestamp = datetime.strptime(parts[0], '%Y-%m-%d')
            employee_code = parts[2]
            booking_splits.append((timestamp, employee_code))
    return booking_splits

def group_bookings_by_day(booking_splits):
    grouped_bookings = defaultdict(list)
    for timestamp, employee_code in booking_splits:
        day_key = timestamp.strftime('%Y-%m-%d')
        grouped_bookings[day_key].append((timestamp, employee_code))
    return grouped_bookings

def print_calendar(grouped_bookings):
    for day, day_bookings in sorted(grouped_bookings.items()):
        print(day)
        for start_time, employee_code in day_bookings:
            print(f"{start_time.strftime('%H:%M')} {employee_code}")
        print()

input_data = [
    "2020-08-17 10:17:06 EMP001",
    "2020-08-21 09:00 2",
    "2020-08-16 12:34:56 EMP002",
    "2020-08-21 09:00 2",
    "2020-08-16 09:28:23 EMP003",
    "2020-08-22 14:00 2",
    "2020-08-17 11:23:45 EMP004",
    "2020-08-22 16:00 1",
    "2020-08-15 17:29:12 EMP005",
    "2020-08-21 16:00 3"
]
booking_splits = parse_booking_data(input_data)
grouped_bookings = group_bookings_by_day(booking_splits)
print_calendar(grouped_bookings)
