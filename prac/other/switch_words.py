def switch_words(s):
    w1 = ""
    w2 = ""
    curr = ""
    w_count = 0
    res = ""
    for i in range(len(s)):
        if s[i] == " ":
            if w_count == 0:
                w1 = curr
                curr = ""
                w_count += 1
            elif w_count == 1:
                w2 = curr
                w_count = 0
                curr = ""
                if res == "":
                    res = w2 +" "+ w1
                else:
                    res += " "+w2+ " " + w1
                w2 = ""
                w1 = ""
        else:
            curr += s[i]
    if w1 != "":
        if curr != "":
            res += " "+curr + " "+ w1
    else:
        res += " "+ curr
    #print res
    return res
print switch_words("ab cd ef gh ij kl")
