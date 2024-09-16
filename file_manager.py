import argparse
import shutil
import os
import logging

def main():
    logging.basicConfig(filename='file_operations.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('-f', '--file', required=True, type=str, nargs=1, help="The file to be managed.")
    group.add_argument('-c', '--copy', type=str, nargs=1, help="The location to copy the file to.")
    group.add_argument('-m', '--move', type=str, nargs=1, help="The location to move the file to.")
    group.add_argument('-r', '--rename', type=str, nargs=1, help="The new name for the file.")
    group.add_argument('-d', '--delete', action="store_true", help="Specifies to delete the file.")
    
    args = parser.parse_args()

    if not args.file[0].strip():
        raise ValueError('Invalid input: file path cannot be empty or whitespace.')

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
            logging.error(f'File {args[0]} does not exist. Please provide a valid file path.')
            raise FileNotFoundError(f'File {args[0]} does not exist. Please provide a valid file path.')
        except OSError:
            logging.error(f'Path: {args[1]} could not be found.')
            raise OSError(f'Path: {args[1]} could not be found.')
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