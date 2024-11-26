import os

file_name = 'my_file.txt'

try:
    # Open the file in read-only mode
    with open(file_name, 'r') as file:
        # Read the entire contents of the file
        content = file.read()
        print('Contents of file:', content)

except FileNotFoundError:
    print('Error: File not found.')

except IOError:
    print('Error: I/O error occurred.')

except Exception as e:
    print('Error:', str(e))