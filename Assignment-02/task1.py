def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
            print(file_contents)
            return file_contents
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

# Example usage:
file_name = "sampletext.txt"
file_contents = read_file(file_name)
if file_contents is not None:
    # You can work with the 'file_contents' string here
    pass

