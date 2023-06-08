import sys

def main():
    operation = sys.argv[1];

    supported_operation = ["reverse", "copy", "duplicate_contents", "replace_string"];

    if operation not in supported_operation:
        print(f"Unsupported operation: {operation}");
        return;

    input_path = input("Input-path is ");

    if operation == "reverse":
        output_path = input("Output-path is ");
        reverse_file(input_path, output_path);
    elif operation == "copy":
        output_path = input("Output-path is ");
        copy_file(input_path, output_path);
    elif operation == "duplicate_contents":
        s = input("How many times will you repeat? ");
        n = int(s);
        duplicate_file(input_path, n);
    elif operation == "replace_string":
        needle = input("Needle is ");
        new_string = input("New string is ");
        replace_string(input_path, needle, new_string);

def read_file(input_path: str) -> str:
    try:
        with open(input_path) as f:
            content = f.read();
            return content;
    except FileNotFoundError:
        raise Exception(f"No file found at {input_path}");    

def write_file(output_path: str, content: str):
    try:
        with open(output_path, "x") as f:
            f.write(content);
    except FileExistsError:
        print(f"File already exsists at {output_path}");

def append_file(input_path: str, content: str):
    try:
        with open(input_path, "a") as f:
            f.write(content);
    except FileNotFoundError:
        print(f"No file found at {input_path}");

def overwrite_file(input_path: str, content: str):
    try:
        with open(input_path, "w") as f:
            f.write(content);
    except FileNotFoundError:
        print(f"No file found at {input_path}");

def reverse_file(input_path: str, output_path: str):
    reversed_content = read_file(input_path)[::-1];
    write_file(output_path, reversed_content);
    

def copy_file(input_path: str, output_path: str):
    content = read_file(input_path);
    write_file(output_path, content);

def duplicate_file(input_path: str, n: int):
    content = read_file(input_path);
    for i in range(0, n):
        append_file(input_path, content);

def replace_string(input_path: str, needle: str, new_string: str):
    content = read_file(input_path);
    content.replace(needle, new_string);
    overwrite_file(input_path, content);

if __name__ == "__main__":
    main();