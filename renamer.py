
# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files


def main():
    pathOfFiles = input("Enter directory : ")
    
    pathOfFiles+="\\"
    for filename in os.listdir(pathOfFiles):
        
        dst = filename[filename.rfind("_")+1:]
        src = pathOfFiles + filename
        dst = pathOfFiles + dst

        # rename() function will
        # rename all the files in the directory
        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()