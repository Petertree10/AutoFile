import argparse
import shutil
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, type=str, nargs=1, help="The file to be managed.")
    parser.add_argument('-c', '--copy', type=str, nargs=1, help="The location to copy the file to.")
    parser.add_argument('-m', '--move', type=str, nargs=1, help="The location to move the file to.")
    parser.add_argument('-r', '--rename', type=str, nargs=1, help="The location to move the file to.")
    parser.add_argument('-d', '--delete', action="store_true", help="Specifies to delete the file.")

    args = parser.parse_args()
    numOfArgs = (args.copy is not None) + (args.move is not None) + (args.rename is not None) + (args.delete)

    if (numOfArgs) > 1:
        parser.error('Too many actions were provided. Please provide only one action at a time.')
    elif (numOfArgs) < 1:
        parser.error('No actions were provided. Add -c or -m or -r or -d.')
    
    if args.copy is not None:
        copyFile(args.file[0], args.copy[0])
    elif args.move is not None:
        moveFile(args.file[0], args.move[0])
    elif args.rename is not None:
        renameFile(args.file[0], args.rename[0])
    elif args.delete is not None:
        deleteFile(args.file[0])

def copyFile(filePath, path):
    try:
        shutil.copy(filePath, path)
    except FileNotFoundError:
        print(f"ERROR: File: {filePath} could not be found.")
    except OSError:
        print(f"ERROR: Path: {path} could not be found.")
        
def moveFile(filePath, path):
    try:
        shutil.move(filePath, path)
    except FileNotFoundError:
        print(f"ERROR: File: {filePath} could not be found.")
    except OSError:
        print(f"ERROR: Path: {path} could not be found.")

def renameFile(filePath, newNamePath):
    try:
        os.rename(filePath, newNamePath)
    except FileNotFoundError:
        print(f"ERROR: File: {filePath} could not be found.")
    
def deleteFile(filePath):
    try:
        os.remove(filePath)
    except FileNotFoundError:
        print(f"ERROR: File: {filePath} could not be found.")


if __name__ == "__main__":
    main()