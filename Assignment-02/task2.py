def read_file_into_list(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

# Example usage:
file_name = "sampletext.txt"
lines = read_file_into_list(file_name)

if lines:
    for line in lines:
        # You can work with each line in the 'lines' list here
        print(line)