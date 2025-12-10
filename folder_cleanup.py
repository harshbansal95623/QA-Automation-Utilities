import os

def cleanup(folder_path):
    files_deleted = 0

    for file in os.listdir(folder_path):
        if file.endswith(".tmp") or file.endswith(".log"):
            os.remove(os.path.join(folder_path, file))
            files_deleted += 1

    print(f"✅ Cleanup complete. Deleted {files_deleted} files.")

if __name__ == "__main__":
    folder = "test_output"
    cleanup(folder)
