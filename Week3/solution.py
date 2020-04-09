def logtolist(log):
    logList = list()
    for line in log:
        currentEntry = dict()
        currentEntry["ip_address"] = line.split(' - - ')[0]
        currentEntry["timestamp"] = line.split('[')[1].split(']')[0]
        currentEntry["request"] = line.split('\"')[1]
        logList.append(currentEntry)
    return logList

def re_logtolist(log):
    logList = list()
    for line in log:
        currentEntry = dict()
        currentEntry["ip_address"] = line.split(' - - ')[0]
        currentEntry["timestamp"] = line.split('[')[1].split(']')[0]
        currentEntry["request"] = line.split('\"')[1]
        logList.append(currentEntry)
    return logList

