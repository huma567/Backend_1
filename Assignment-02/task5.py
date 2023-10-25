def read_file_in_reverse(file_name):
    try:
        reversed_lines = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            reversed_lines = list(reversed(lines))
            for line in reversed_lines:
                print(line, end='')  # Print each line without an extra newline character

        return reversed_lines
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

# Example usage:
file_name = "sampletext.txt"
reversed_lines = read_file_in_reverse(file_name)

if reversed_lines:
    # You can work with the reversed lines in the 'reversed_lines' list here
    pass