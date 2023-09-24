import os


def get_file_path_from_user():
    file_path = input("Please enter the path to the file: ")

    if os.path.exists(file_path) and os.path.isfile(file_path):
        print("File exists!")
        return file_path
    else:
        print("File does not exist or the path is incorrect. Please try again.")
        return None

