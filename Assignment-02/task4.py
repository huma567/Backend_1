def read_even_numbered_lines(file_name):
    try:
        even_lines = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i in range(1, len(lines), 2):  # Start at the second line (0-based index) and skip every other line
                even_lines.append(lines[i])
        return even_lines
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

# Example usage:
file_name = "sampletext.txt"
even_lines = read_even_numbered_lines(file_name)

if even_lines:
    for line in even_lines:
        # You can work with each even line in the 'even_lines' list here
        print(line)