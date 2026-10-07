import os
import shutil

SOURCE_FOLDER = "test_files"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Python": [".py"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Excel": [".xls", ".xlsx", ".csv"]
}


def organize_files():

    if not os.path.exists(SOURCE_FOLDER):
        print("Source folder does not exist.")
        return

    for filename in os.listdir(SOURCE_FOLDER):

        file_path = os.path.join(SOURCE_FOLDER, filename)

        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()

        destination_folder = "Others"

        for category, extensions in FILE_TYPES.items():

            if extension in extensions:
                destination_folder = category
                break

        destination_path = os.path.join(
            SOURCE_FOLDER,
            destination_folder
        )

        os.makedirs(destination_path, exist_ok=True)

        shutil.move(
            file_path,
            os.path.join(destination_path, filename)
        )

        print(f"Moved {filename} → {destination_folder}")


if __name__ == "__main__":
    organize_files()