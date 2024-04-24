def read(filename):
    file = open(filename)
    rows = file.readlines()
    file.close()
    return rows

def process(rows, first = 0, last = 0):
    numbers=[]
    for i in range(first,len(rows)-last):
        numbers.append(int(rows[i].strip()))
    return numbers

"""
def process_space(string, separator=" ", first = 0, last = 0):
    onerow=string.split(separator)
    numbers=process(onerow[first:len(onerow)-last])
    return numbers
"""

def process_space(string, separator=" ", first = 0, last = 0, dataseparator = None):
    onerow=string.split(separator)
    if dataseparator is not None:
        onerow=onerow[first:len(onerow)-last][0].split(dataseparator)
        numbers=process(onerow)
    else:
        numbers=process(onerow[first:len(onerow)-last])
    return numbers