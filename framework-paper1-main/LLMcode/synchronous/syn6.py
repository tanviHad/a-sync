import random
from datetime import datetime, timedelta

def random_date(start, end):
    """
    Generate a random date between two datetime objects.
    """
    delta = end - start
    random_days = random.randrange(delta.days)  # Generate a random number of days
    date = start + timedelta(days=random_days)  # Add the random number of days to the start date
    return date.strftime('%m/%d/%Y')  # Format the date to match toLocaleDateString() output

# Define the start and end dates
start = datetime(2020, 1, 1)
end = datetime(2020, 1, 7)

# Generate a random date
print(random_date(start, end))
