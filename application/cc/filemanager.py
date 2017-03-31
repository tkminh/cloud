import os
import os.path

def get_file_content(_fname):
    file = os.getcwd() + '/' + _fname
    if os.path.isfile(file) == False:
        print fname + " is not found."
        return None
    with open(file, 'r') as f:
        data=f.read().replace('\n', '')
    return data