n = "sridhar"
without_repitation = ""
for j in n:
    if j not in without_repitation:
        without_repitation += j
for i in without_repitation:
    print("{} repeated {} times".format(i,n.count(i)))