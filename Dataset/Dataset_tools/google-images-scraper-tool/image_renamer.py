import os


def rename_files_in_folders(base_path):
    folders = [
        d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))
    ]
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        files = os.listdir(folder_path)
        for filename in files:
            old_file_path = os.path.join(folder_path, filename)
            if os.path.isfile(old_file_path):
                new_filename = f"{folder}_{filename}"
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{old_file_path}' to '{new_file_path}'")


base_path = "Dataset/Dataset_tools/scraped_images/dataset_1/"
rename_files_in_folders(base_path)
