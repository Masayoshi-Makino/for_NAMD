import string_changer as sc
#If you want to use this module, you must need string_changer.py.
#Maybe, you can get string_changer.py from repository containing this module.

inpfilename = input("Please enter the file name you want to use.\n")
inpfile = open(inpfilename, "r")
#Open the pdb file containing watar box of TIP3 water.

waterline = []
#Create the new list.

for i in inpfile:
    line = i.split()
    print(line)
    if len(line) < 5:
        pass
    elif line[2] == "OH2":
        waterline.append(i)
    else:
        pass

inpfile.close()
#Extract rows containing string "OH2".

print(waterline)

cnt = 1
for j in range(len(waterline)):
    waterline[j] = sc.strchanger(waterline[j], 22, " ")
    waterline[j] = waterline[j].split()
    if waterline[j][10] != waterline[j - 1][10]:
        cnt = 1
    else:
        pass
    waterline[j][1] = str(cnt)
    waterline[j][3] = "TP4EW"
    waterline[j][4] = str(cnt)
    cnt += 1
#Processing list.

for k in range(len(waterline)):
    waterline[k][1] = waterline[k][1].rjust(7)
    waterline[k][2] = waterline[k][2].center(6)
    waterline[k][4] = waterline[k][4].rjust(4)
    waterline[k][5] = waterline[k][5].rjust(12)
    waterline[k][6] = waterline[k][6].rjust(8)
    waterline[k][7] = waterline[k][7].rjust(8)
    waterline[k][8] = waterline[k][8].rjust(6)
    waterline[k][9] = waterline[k][9].rjust(6)
    waterline[k][10] = waterline[k][10].rjust(9)
    waterline[k][11] = waterline[k][11].rjust(3)
    waterline[k] = "".join(waterline[k])
#My practice of rjust method.

outfilename = input("Please enter the new file name.\n")
outfile = open(outfilename, "w")
outfile.write("\n".join(waterline))
outfile.close()
#Writing file.