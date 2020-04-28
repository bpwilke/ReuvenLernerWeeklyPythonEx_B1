import os
from os import listdir
from os.path import isfile, join

def file_length(filename):
    return os.stat(filename).st_size

def filefunc(path, func):
    success = dict()               #<-- initialize successes
    fail = dict()                  #<-- initialize failures
    onlyfiles = [file for file in listdir(path) if isfile(join(path, file))] # get list of files
    for file in onlyfiles:         #<-- for each of our files
        try:                       #<-- try and apply our function
            success[file] = file_length(join(path, file)) # if successful add to success dict
        except Exception as e:
            fail[file] = e         # if fails, add exception obj to fail dict
    return success, fail           # return both dicts


if __name__ == '__main__':
	my_success, my_failure = filefunc('/Users/bwilke/Desktop/', file_length)
	print(f'Successes: \n {my_success} \n Failures: \n {my_failure}')