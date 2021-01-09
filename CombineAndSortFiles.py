import glob

def readFile(fileType, outFile, doSortFile):

    read_files = glob.glob("*." + fileType)

    with open(outFile + "." + fileType, "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

    if doSortFile == True:
        with open(outFile + "." + fileType, 'r') as r:
            with open(outFile + "_sorted" +"." + fileType, "w") as outfile:
                for line in sorted(r):
                    outfile.write(line)

def main():
    # if len(sys.argv) > 0:
    #     setParams()
    fileType = input("Set file type? #type 'txt' or 'csv': ")
    outFile = input("Set out file name #type the file name without an extension: ")
    doSortFile = input('Sort the out file lines alphabetically? #type y or n: ')
    if (doSortFile.upper() == 'Y') or (doSortFile.upper() == 'YES'): 
        doSortFile = True

    readFile(fileType, outFile, doSortFile)

main()