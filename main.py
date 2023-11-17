def load_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print("An error occurred while reading a file:", e)
        return None

def save_text_file(file_path, text):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
            print("Spaces are successfully removed and the result is saved in the", file_path)
    except Exception as e:
        print("An error occurred while saving the file:", e)

def remove_spaces(text):
    if text is not None:
        return text.replace(' ', '')
    return None

if __name__ == "__main__":
    file = "text.txt"
    string = load_text_file(file)
    save_text_file(file_path="result.txt", text=remove_spaces(string))
    