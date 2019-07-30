d=[ ("fizz", 3), ("buzz", 5), ("fuzz", 7), ("bizz", 9)]
i = 0
for i in range (1, 101):
    s = ""
    for x in range (len(d)):
        if i % d[x][1] == 0:
            s = s + d[x][0]
    if s == "":
        s = int(i)
    print(s)