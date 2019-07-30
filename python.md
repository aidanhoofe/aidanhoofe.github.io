# Python
**FizzBuzz:** Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".



```
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
```
[fizzbuzz.py](/fizzbuzz.py)

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
