import sys
filename = str(sys.argv[1])
plant_code = filename.split(".")[0].split("_")[3]
file_read = open(filename, "r+")
op=""
for line in file_read:
    if line != "":
        array = line.split("|")
        if len(array) == 5:
            i=1
            op = op + plant_code + "|" + array[1].strip() + "|" + array[2].strip() + "|" + array[3].strip() + "|" + array[4].strip() +  "\n"
        else:
            op = op + plant_code + "|" + line.strip() + "\n"
file_read.close()
file_write = open(filename, "w")
file_write.write(op)
file_write.close()
