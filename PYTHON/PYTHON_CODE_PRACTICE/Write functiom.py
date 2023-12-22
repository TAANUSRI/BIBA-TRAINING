def write_to_file(file_path, content):
    """Write content to a file."""
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print("Content successfully written to the file.")
    except Exception as e:
        print(f"Error: {e}")
file_path = "C:/Users/WINDOWS/Desktop/Assignments/Python_practice/example.txt"
file_content = "Hello, this is some content to write to the file."
write_to_file(file_path, file_content)

