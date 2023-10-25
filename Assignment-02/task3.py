def write_first_line_to_file(file_contents, output_filename):
    try:
        # Determine the first line by splitting the contents at the first newline character
        first_line = file_contents.split('\n', 1)[0]
        
        with open(output_filename, 'w') as output_file:
            output_file.write(first_line)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_contents = "This is the first line.\nThis is the second line.\nThis is the third line."
output_filename = "output.txt"

write_first_line_to_file(file_contents, output_filename) 