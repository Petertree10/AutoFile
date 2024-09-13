import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, type=str, nargs=1, help="The file to be managed.")
    parser.add_argument('-c', '--copy', type=str, nargs=1, help="The location to copy the file to.")
    parser.add_argument('-m', '--move', type=str, nargs=1, help="The location to move the file to.")
    parser.add_argument('-r', '--rename', type=str, nargs=1, help="The location to move the file to.")
    parser.add_argument('-d', '--delete', type=str, nargs=1, help="Specifies to delete the file.")

    args = parser.parse_args()
    numOfArgs = (args.copy is not None) + (args.move is not None) + (args.rename is not None) + (args.delete is not None)

    if (numOfArgs) > 1:
        parser.error('Too many actions were provided. Please provide only one action at a time.')
    elif (numOfArgs) < 1:
        parser.error('No actions were provided. Add -c or -m or -r or -d.')
    

#def copyFile():

#def moveFile():

#def renameFile():

#def deleteFile():


if __name__ == "__main__":
    main()