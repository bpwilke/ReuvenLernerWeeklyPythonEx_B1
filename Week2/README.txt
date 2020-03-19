You're probably familiar with the "range" function in Python.  In Python 2, it returns a list:
    >>> range(5)
    [0, 1, 2, 3, 4]

    >>> range(5,10)
    [5, 6, 7, 8, 9]

    >>> range(5,20,3)
    [5, 8, 11, 14, 17]

In Python 3, "range" returns an iterator object -- the same sort of object as "xrange" returned in Python 2:
    >>> range(5)
    range(0, 5)

    >>> range(5,10)
    range(5, 10)

    >>> range(5,20,3)
    range(5, 20, 3)

This week, I want you to implement "myrange", our own home-grown version of the built-in "range" function.

Should you implement it Python 2 style, such that it returns a list, or Python 3 style, such that it returns an iterator?

The answer is: Yes!  I'd like you to implement both, so that you can see the difference between returning a list (potentially long) and returning an iterator.

That is, I'd like you to implement:
A function ("myrange2") that takes one, two, or three parameters and returns a list that looks like my above examples for Python 2's "range" functio.
A generator function ("myrange3") that takes one, two, or three parameters and returns an iterator (well, a generator) that looks like my above examples for Python 3's "range" function.  Note that the printed representation doesn't have to look the same.
In both cases, it should be possible to take the output of calling our function and stick it into a "for" loop:
    for x in myrange2(10, 30, 3):
        print(x)

The above should print
    10 13 16 19 22 25 28

We should get the same result from invoking:
    for x in myrange3(10, 30, 3):
        print(x)


I'll be back on Monday with a solution.

Reuven