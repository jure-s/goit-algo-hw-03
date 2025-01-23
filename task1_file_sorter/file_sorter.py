import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Sort files by extension into directories.")
    parser.add_argument("source_dir", type=str, help="Path to the source directory.")
    parser.add_argument(
        "destination_dir", type=str, nargs="?", default="dist", help="Path to the destination directory (default: dist)."
    )
    return parser.parse_args()

def create_directory(path):
    """Create a directory if it doesn't exist."""
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {path}: {e}")


def copy_files_by_extension(source_dir, destination_dir):
    """Recursively copy files from source_dir to destination_dir and sort by file extension."""
    try:
        for root, _, files in os.walk(source_dir):
            for file in files:
                source_file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1].lstrip(".").lower()

                # If no extension, place in 'others'
                if not file_extension:
                    file_extension = "others"

                target_dir = os.path.join(destination_dir, file_extension)
                create_directory(target_dir)

                target_file_path = os.path.join(target_dir, file)
                try:
                    shutil.copy2(source_file_path, target_file_path)
                    print(f"Copied: {source_file_path} -> {target_file_path}")
                except IOError as e:
                    print(f"Error copying file {source_file_path}: {e}")

    except Exception as e:
        print(f"Error during processing: {e}")


def main():
    args = parse_arguments()

    source_dir = args.source_dir
    destination_dir = args.destination_dir

    if not os.path.exists(source_dir):
        print(f"Source directory does not exist: {source_dir}")
        return

    create_directory(destination_dir)
    copy_files_by_extension(source_dir, destination_dir)

if __name__ == "__main__":
    main()
