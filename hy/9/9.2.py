import os

for folderName, subfolders, filenames in os.walk("."):
    print(f"Current folder: {folderName}")

    for subfolder in subfolders:
        print(f"SUBFOLDER OF {folderName}: {subfolder}")

    for filename in filenames:
        print(f"FILE INSIDE {folderName}: {filename}")

    print("")  # Print a newline for better readability
