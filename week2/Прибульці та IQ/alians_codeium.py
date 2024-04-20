"""Faster and more efficient solution to the problem

ерор Exception has occurred: TypeError
'>=' not supported between instances of 'int' and 'str'"""
import time
from memory_profiler import profile

start_time = time.time()
def read_file(file_path:str)->dict:
    """
    Reads and returns a dictionary with names and their IQs
    from the given file path.
    Example of file content:
    Elon Musk,165
    Mark Zuckerberg,152
    should return {'Elon Musk': 165, 'Mark Zuckerberg': 152} where values are integers
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
    ...     _=tmp.write('#data from blabla\\nWill Smith,157\\nBill Gates,160')
    ...     _=tmp.seek(0)
    ...     print(read_file(tmp.name))
    {'Will Smith': 157, 'Bill Gates': 160}
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.readlines()
    data = [i.strip().split(',') for i in data[1:]]
    dct = {}
    for i in data:
        dct[i[0]] = int(i[1])
    return dct

def rescue_people(smarties:dict, limit_iq:int)->tuple:
    """
    Returns a list of people who can be rescued.
    smartiess is a dictionary with names and their IQs 
    for instance {'Elon Musk': 165, 'Mark Zuckerberg': 152}
    and limit_iq is used to determine who can be rescued
    >>> rescue_people({"Conan O'Brien": 160, 'Bill Gates':160}, 200)
    (2, [['Bill Gates'], ["Conan O\'Brien"]])
    """
    if not smarties:
        return 0, []

    names = sorted(smarties.items(), key=lambda x: (-x[1], x[0]))
    res = []
    amount = 0

    while names:
        current = 0
        res.append([])
        names_to_remove = []

        for idx, (name, iq) in enumerate(names):
            if limit_iq - current < 0:
                break
            if limit_iq - current >= iq:
                res[amount].append(name)
                current += iq
                names_to_remove.append(idx)

        names = [names[i] for i in range(len(names)) if i not in names_to_remove]
        amount += 1

    return len(res), res

@profile
def main():
    dct = read_file('week2\\Прибульці та IQ\\smart_people.txt')
    print(dct)
    res = rescue_people(dct, 200)
    print(res)

main()
print("--- %s seconds ---" % (time.time() - start_time))
