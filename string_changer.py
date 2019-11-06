def strchanger(targetstring, index, substitute):
    strlist = []
    for i in targetstring:
        strlist.append(i)
    strlist[index] = substitute
    return "".join(strlist)