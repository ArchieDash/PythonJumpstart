import os
import subprocess
import platform
import cat_service


def main():
    print_header()
    folder = get_output_folder()
    download_cats(folder)
    display_cats(folder)


def print_header():
    print("---------------------")
    print("     CAT FACTORY     ")
    print("---------------------")
    

def get_output_folder():
    base_folder = os.path.abspath(os.path.dirname(__file__))
    folder = "cat_pictures"
    full_path = os.path.join(base_folder, folder)
    if not os.path.exists(full_path):
        print(f"Creating new directry at {base_folder}")
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    print("Contacting server to download cats...")
    cat_count = 10
    for i in range(1, cat_count+1):
        name = f"lolcat {i}"
        print("Downloading cat " + name)
        cat_service.get_cat(folder, name)
    print("DONE")
    
    
def display_cats(folder):
    if platform.system() == "Dwarwin":
        subprocess.call(["open", folder])
    elif platform.system() == "Windows":
        subprocess.call(["explorer", folder])
    elif platform.system() == "Linux":
        subprocess.call(["xdg-open", folder])
    else:
        print(f"LOLcat factory does't support {platform.system()}")
    

if __name__ == "__main__":
    main()