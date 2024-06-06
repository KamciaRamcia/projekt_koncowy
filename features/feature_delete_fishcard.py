import os


def deleteAllElements(dictionary_name):
    path_to_file = f"../all_fishcards/{dictionary_name}"
    print(path_to_file)
    if os.path.isfile(path_to_file):
        os.unlink(path_to_file)