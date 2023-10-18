from datetime import datetime, timedelta
from collections import defaultdict

def edit_booking_data(data):
    bookings = []
    for l in data:
        dt = l.split()
        if len(dt) == 3:
            try:
                timestamp = datetime.strptime(dt[0] + ' ' + dt[1], '%Y-%m-%d %H:%M:%S')
            except ValueError:
                timestamp = datetime.strptime(dt[0], '%Y-%m-%d')
            emp_code = dt[2]
            bookings.append((timestamp, emp_code))
    return bookings

def group_bookings(bookings):
    grouped_bookings = defaultdict(list)
    for timestamp, emp_code in bookings:
        day_key = timestamp.strftime('%Y-%m-%d')
        grouped_bookings[day_key].append((timestamp, emp_code))
    return grouped_bookings

def print_calendar(grouped_bookings):
    for day, bookings in sorted(grouped_bookings.items()):
        print(day)
        for start, emp_code in bookings:
            print(f"{start.strftime('%H:%M')} {emp_code}")
        print()


inp_data = [
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
bookings = edit_booking_data(inp_data)
grouped_bookings = group_bookings(bookings)
print_calendar(grouped_bookings)