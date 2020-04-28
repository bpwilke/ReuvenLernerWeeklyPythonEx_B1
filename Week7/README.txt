This week, we'll write a function that takes a function as an argument.  Actually, the function takes two arguments:
A directory name (string)
a function

The function will be applied to each file in the directory.

The output from the function's execution on each file will be returned as part of a dictionary, in which the filenames are the keys and the results are the values.

For example, if we call
    import os

    def file_length(filename):
    return os.stat(filename).st_size

    success_dict, failure_dict = filefunc('/etc/', file_length)

The result will be two dictionaries:
- The first dictionary's keys are the filenames and the output from running the function, when no exception was raised, and
- The second dictionary's keys are the filenames and the exception object when one was raised.

So in the above call, if no exceptions were raised, then the first dictionary returned would consist of the fienames in /etc/, with the length of each file as a value.  The second dictionary would be empty.

I'm afraid that there isn't any test this week; I'm very much open to ideas on how to use pytest to check files in a directory.  Let me know what you think!

And in any event, you can discuss this assignment in the forums.

I'll be back on Monday with a solution.

Reuven