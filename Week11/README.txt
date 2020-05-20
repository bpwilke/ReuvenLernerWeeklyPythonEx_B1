This week, we'll look at another way in which we can use Python's magic methods to create an object that takes use of built-in operators. This week, we're going to create a class that I call DirFIleHash. The idea is that you create an instance of DirFileHash by passing a directory name:

    d = DirFileHash('/etc/')

You can then get the MD5 hash of any file in this directory by putting it in square brackets:

    print(d['passwd'])

This will return the 32-character hexadecimal MD5 hash value for the contents of /etc/passwd.

You'll almost certainly want to use Python's "hashlib" in order to solve this exercise, which is documented here:

    https://docs.python.org/3/library/hashlib.html

If you pass a value that doesn't exist, or isn't a file, or isn't a legitimate thing that you can open and read the contents from, then the method should return None.

Questions or comments?  Post them to the forum!

I'll provide answers and tips on Monday.

Until then,

Reuven
