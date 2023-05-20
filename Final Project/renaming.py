# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os
import time
root = "/Users/waynsday/PycharmProjects/MFAIMFG/Final Project/data2/test/2/"
# Function to rename multiple files

def main():

    for count, filename in enumerate(os.listdir(root)):
        dst = "car." + str(count) + ".jpg"
        src = root + filename
        dst = root + dst
        print(count)

        # rename() function will
        # rename all the files
        os.rename(src, dst)

    # Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()