import re


def main():
    print(convert(input("Hours: ")))

## Defining convert we are given the challenge of parsing the input to be able to tell the time
## We then need to create a few variables we can use to check different elements of our code
#### We also need to be able to check our answers for the same code validity.

def convert(s):
    pattern = r'([0-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([0-9]|1[0-2])(:[0-5][0-9])? (AM|PM)'
    match = re.match(pattern, s.strip(), re.IGNORECASE)

    if not match:
        raise ValueError("Invalid time format")

    start_hour, start_minute = match.group(1), match.group(2) or ":00"
    start_period = match.group(3).upper()
    end_hour, end_minute = match.group(4), match.group(5) or ":00"
    end_period = match.group(6).upper()

## To be able to get this code working I had to contain my definition for 24 hour conversion within the convert function and then link that to the test cases
## Check50 was showing me that by giving two separate functions I was making things too spread out and needed to allow check50 to run my code in the established archetecture from the problem set.
    def to_24_hour(hour, minute, period):
        hour = int(hour)
        minute = int(minute[1:])  # Remove the colon

        if period == "PM" and hour != 12:
            hour += 12
        elif period == "AM" and hour == 12:
            hour = 0

        return f"{hour:02d}:{minute:02d}"

    start_24 = to_24_hour(start_hour, start_minute, start_period)
    end_24 = to_24_hour(end_hour, end_minute, end_period)

    return f"{start_24} to {end_24}"


if __name__ == "__main__":
    main()
