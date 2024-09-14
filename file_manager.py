import argparse
import shutil
import os
import logging

def main():
    logging.basicConfig(filename='file_operations.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

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
        copy_file(args.file[0], args.copy[0], action = 'Copied')
    elif args.move is not None:
        move_file(args.file[0], args.move[0], action = 'Moved')
    elif args.rename is not None:
        rename_file(args.file[0], args.rename[0], action = 'Renamed')
    elif args.delete:
        delete_file(args.file[0], action = 'Deleted')            

def logging_manager(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            action = kwargs.get('action', 'Operation')
            logging.info(f'{action} file {os.path.basename(args[0])} successfully.')
        except FileNotFoundError:
            logging.error(f'File: {args[0]} could not be found.')
            exit()
        except OSError:
            logging.error(f'Path: {args[1]} could not be found.')
            exit()
    return wrapper
    
@logging_manager
def copy_file(filePath, path, **kwargs):
    shutil.copy(filePath, path)

@logging_manager
def move_file(filePath, path, **kwargs):
    shutil.move(filePath, path)

@logging_manager
def rename_file(filePath, newName, **kwargs):
    newPath = os.path.join(os.path.dirname(filePath), newName)
    os.rename(filePath, newPath)

@logging_manager
def delete_file(filePath, **kwargs):
    os.remove(filePath)

if __name__ == "__main__":
    main()