#gender
#mapper.py
Mapper.py
#!/usr/bin/env python

import sys
import csv

column_index = 2  # Set the index of the column you want (3rd column in this example)

# Mapper function
for line in sys.stdin:
    # Use the CSV reader to parse the input line
    csv_reader = csv.reader([line])
    fields = next(csv_reader)  # Get the fields of the CSV row as a list

    if len(fields) > column_index:
        gender = fields[column_index]

        # Emit the gender as the key with a count of 1 as the value
        print(f'{gender}\t1')

#reducer
#!/usr/bin/env python

import sys

gender_count = {'1': 0, '2': 0}

# Reducer function
for line in sys.stdin:
    gender, count = line.strip().split('\t')
    gender_count[gender] += int(count)

# Output the counts for each gender
for gender, count in gender_count.items():
    print(f'Gender: {gender}, Count: {count}')

#age
#mapper
#!/usr/bin/env python

import sys

# Mapper function
for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    # Assuming 'age' is in the first column
    if len(fields) >= 1:
        age = fields[0]

        # Emit the key-value pairs for 'age' only
        print(f'{age}\t1')

#reducer
#!/usr/bin/env python

import sys

current_age = None
age_count = 0

# Reducer function
for line in sys.stdin:
    line = line.strip()
    age, count = line.split('\t')
    count = int(count)

    if current_age is None:
        current_age = age

    # If the age changes, output the count for the previous age
    if age != current_age:
        print(f'Age: {current_age}, Count: {age_count}')
        current_age = age
        age_count = 0

    # Sum the counts for each age group
    age_count += count

# Output the count for the last age group
if current_age is not None:
    print(f'Age: {current_age}, Count: {age_count}')
