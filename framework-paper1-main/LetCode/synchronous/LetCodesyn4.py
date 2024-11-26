def file_read(fname):
    try:
        with open(fname, 'r') as file:  # 'r' mode is default and can be omitted, but it's good to be explicit
            print(file.read())
    except FileNotFoundError:
        print(f"The file {fname} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

file_read('C:/frameworkpaper1/monitore.txt')
