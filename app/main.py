import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) < 3 or command_parts[0] != "mv":
        return
    command_type, input_file, others = command_parts
    *dirs, output_file = others.split("/")
    if dirs:
        os.makedirs("/".join(dirs), exist_ok=True)
    try:
        with (
            open(input_file) as file_from,
            open(others, "w") as file_to
        ):
            file_to.write(file_from.read())
        os.remove(input_file)
    except FileNotFoundError:
        return
