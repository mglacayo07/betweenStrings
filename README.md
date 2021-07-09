# Between String

If we want to make a generic message we can do something like this "Hello ${name}! your brithday is on ${birthday}"

Imagine that the words between ${this} will be replace with the information, but if we don't have the information it will be send with the ${keys}

This function will replace the words that wasn't replace with a generic message.

<pre>
def betweenStrings(txt,name,birthday):

    if name != "":
        txt = txt.replace("${name}", name)
    if birthday != "":
        txt = txt.replace("${birthday}", birthday)

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
    txt = "Hello ${name}! your brithday is on ${birthday}"
    name = input("Name: ")
    brithday = input("Birthday: ")
    print(betweenStrings(txt,name,brithday))

</pre>
# Technologies

* Python 3.8

# Preview

![](https://github.com/mglacayo07/betweenStrings/blob/dev/preview.png)
