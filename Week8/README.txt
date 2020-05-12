This week, we'll be writing another generator function. (Oh, goody!) Normally, an iterator returns the elements of its inputs one at a time. This week, I want to take several inputs (similar to itertools.chain) but return their elements interleaved (like "zip").

In fact, I call it: multiziperator!

(Don't like the name? Fine, it's only for one week.)
    letters = 'abcde'
    numbers = [1,2,3,4,5]
    symbols = '!@#$%'

    for one_item in multiziperator(letters, numbers, symbols):
        print(one_item)

The result would be:
   a
    1
    !
    b
    2
    @
    c
    3
    #
    d
    4
    $
    e
    5
    %

In other words: We get the first element of "letters", then the first element of "numbers", then the first element of "symbols".  Then the second element of each.  Then the third element of each.  And so forth.

You should be able to pass any number of iterables to multiziperator.  And if they aren't the same length, then the shortest one determines when things stop.

Questions or comments?  Use the forum!  I'll be back on Monday with a solution.

Reuven
