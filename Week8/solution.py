def multiziperator(*args):
    min_len = min([len(each) for each in args])   #<-- figure out the smallest length'd sequence
    idx = 0
    while idx < min_len:
        for iterable in args:
            yield str(iterable[idx])
        idx += 1