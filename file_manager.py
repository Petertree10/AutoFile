import argparse
import shutil
import os
import logging

def main():
    logging.basicConfig(filename='file_operations.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    
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
        logging.error(f'File: {filePath} could not be found.')
    except OSError:
        logging.error(f'Path: {path} could not be found.')
    logging.info(f'Copied file {os.path.basename(filePath)} to {path}')
        
def moveFile(filePath, path):
    try:
        shutil.move(filePath, path)
    except FileNotFoundError:
        logging.error(f'File: {filePath} could not be found.')
    except OSError:
        logging.info(f'Path: {path} could not be found.')
    logging.info(f'Moved file {os.path.basename(filePath)} to {path}')

def renameFile(filePath, newName):
    try:
        newPath = os.path.join(os.path.dirname(filePath), newName)
        os.rename(filePath, newPath)
    except FileNotFoundError:
        logging.error(f'File: {filePath} could not be found.')
    logging.info(f'Renamed file {os.path.basename(filePath)} to {newName}')
    
def deleteFile(filePath):
    try:
        os.remove(filePath)
    except FileNotFoundError:
        logging.error(f'File: {filePath} could not be found.')
    print(f'Successfully deleted file {os.path.basename(filePath)}')

if __name__ == "__main__":
    main()