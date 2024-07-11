def save_first_3000_lines(file_path):
    first_3000_file_path = f"{file_path}_first_3000_lines.txt"
    line_count = 3000

    with open(file_path, "r") as file, open(
        first_3000_file_path, "w"
    ) as first_3000_file:
        for _ in range(line_count):
            line = file.readline()
            if not line:
                break
            first_3000_file.write(line)

    print(f"First 3000 lines of '{file_path}' saved into '{first_3000_file_path}'.")


# Example usage
save_first_3000_lines("uccserverdata.txt")
