def myrange2(start, end=None, step=None):
    outList = list()
    if start and end and step:
        while start < end:
            outList.append(start)
            start += step
    elif start and end:
        while start < end:
            outList.append(start)
            start += 1
    elif start:
        startOnly = 0
        while startOnly < start:
            outList.append(startOnly)
            startOnly += 1
    return outList

def myrange3(start, end=None, step=None):
    if start and end and step:
        while start < end:
            yield start
            start += step
    elif start and end:
        while start < end:
            yield start
            start += 1
    elif start:
        startOnly = 0
        while startOnly < start:
            yield startOnly
            startOnly += 1





