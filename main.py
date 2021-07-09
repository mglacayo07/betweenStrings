
def betweenStrings(txt,name,birthday):

    print("The original string is : " + str(txt))
    if name != "":
        txt = txt.replace("${name}", name)
    if birthday != "":
        txt = txt.replace("${birthday}", birthday)

    print("Replacing the keys : " + str(txt))

    # initializing keys strings
    keys = ["${","}"]

    idx1 = 1
    while idx1 > 0:
        if keys[0] in txt:
            idx1 = txt.index(keys[0])
        else:
            idx1 = -1

        if keys[1] in txt:
            idx2 = txt.index(keys[1])

        str = ''
        if idx1 > 0:
            # getting elements in between
            for idx in range(idx1 + len(keys[0]), idx2):
                str = str + txt[idx]
            if str in txt:
                txt = txt.replace("${" + str + "}", "NO DATA")

    return txt

if __name__ == '__main__':
    txt = "Hello ${name}! your brithday is on ${birthday}"
    name = input("Name: ")
    brithday = input("Birthday: ")
    print(betweenStrings(txt,name,brithday))
    print()
    txt = "Hello ${name}! your brithday is on ${birthday}"
    name = input("Name: ")
    brithday = input("Birthday: ")
    print(betweenStrings(txt,name,brithday))
