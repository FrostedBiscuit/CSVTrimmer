import sys
import os.path

def trim_csv():

    if len(sys.argv) == 1:
        print("No csv file to trim specified, usage: python csv_trimmer.py *filepath*")
        return

    if os.path.exists(sys.argv[1]) == False:
        print(f"Path {sys.argv[1]} is invaild.")
        return

    element_split_char = "," #str(input("Enter the split character: "))
    
    file_to_read = open(sys.argv[1], "r")

    data = [[element.strip(" \n") for element in line.split(element_split_char)] for line in file_to_read.readlines()]
    header = list(filter(None, data[0]))

    file_to_read.close()

    file_to_write = open(f"{sys.argv[1]}", "w")

    print(f"{element_split_char} ".join(header), file=file_to_write)

    for i in range(1, len(data)):
        print(f"{element_split_char} ".join(data[i][0:len(header)]), file=file_to_write)

    file_to_write.close()

trim_csv()