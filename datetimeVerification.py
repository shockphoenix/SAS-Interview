def date_file_verification(input_file, output_file):
    # Reads an input_file of strings separated by lines, and checks them against thie ISO 8601 Date Format
    # Stores valid dates to a set to insure there are only unique Date/Time Values
    # Writes the set once finished to a new output_file
    date_set = set()
    with open(input_file, 'r') as file1:
        for line in file1:
            if iso_verification(line.rstrip()):
                date_set.add(line.rstrip())
        file1.close()
    with open(output_file, 'w') as file2:
        for line in date_set:
            file2.write(line+'\n')
        file2.close()

def iso_verification(date_time):
    # Takes a string and checks to verify it is a valid ISO 8601 Date Format
    if not((len(date_time) == 20 or len(date_time) == 25) and isinstance(date_time, str)):
        return False
    date_string = date_time[0:10]
    time_string = date_time[10:19]
    tzd_string = date_time[19:]
    return date_verification(date_string) and time_verification(time_string) and tzd_verification(tzd_string)

def date_verification(date_string):
    # Takes a date string to verify it is in the correct format of YYYY-MM-DD
    # Verifies the date is part of the 12 months, and verifying less than 31 days, Does not verify against 28/30 day months
    if len(date_string) != 10:
        return False
    year = date_string[0:4]
    month = date_string[5:7]
    day = date_string[8:10]
    dashes = (date_string[4]+date_string[7]) == '--'
    if (year+month+day).isnumeric() and dashes:
        if (0 < int(month) <= 12 and 0 < int(day) <= 31):
            return True
    return False

def time_verification(time_string):
    # Takes a time String starting with 'T' and making sure it is in the format THH:mm:ss
    if len(time_string) != 9:
        return False
    hour = time_string[1:3]
    minute = time_string[4:6]
    second = time_string[7:9]
    form = (time_string[0]+time_string[3]+time_string[6]) == 'T::'
    if (hour+minute+second).isnumeric() and form:
        if( int(hour) < 24 and int(minute) < 60 and int(second) < 60):
            return True
    return False

def tzd_verification(tzd_string):
    # Takes a Time Zone Designator string and verifies it is either 'Z' for GMT or (+/-)HH:mm
    if tzd_string == 'Z':
        return True
    if len(tzd_string) != 6:
        return False
    hour = tzd_string[1:3]
    minute = tzd_string[4:6]
    form = (tzd_string[0]+ tzd_string[3]) == '+:' or (tzd_string[0]+ tzd_string[3]) == '-:'
    if (hour+minute).isnumeric() and form:
        if( int(hour) < 24 and int(minute) < 60):
            return True
    return False