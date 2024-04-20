"""IQ"""
import time
from memory_profiler import profile
start_time = time.time()

def quick_sort(lst:list, k)->list:
    """
    sort the list of tuples commparing its k element
    from max to min using quick sort algorithm
    and from a to z if k=0
    >>> quick_sort([('a', 5), ('b', 1), ('c', 6), ('d', 4), ('e', 2)], 1)
    [('c', 6), ('a', 5), ('d', 4), ('e', 2), ('b', 1)]
    >>> quick_sort([('a', 5), ('b', 1), ('c', 6), ('d', 4), ('e', 2)], 0)
    [('a', 5), ('b', 1), ('c', 6), ('d', 4), ('e', 2)]
    """
    if len(lst)<=1:
        return lst
    pivot=lst[-1]
    l1=[]
    l2=[]
    for i in lst[:-1]:
        if i[k]>pivot[k] and k==1:
            l1.append(i)
        elif i[k]<pivot[k] and k==0:
            l1.append(i)
        else:
            l2.append(i)
    return quick_sort(l1,k)+[pivot]+quick_sort(l2,k)

def read_file(file_path:str)->dict:
    """
    return a dictionary with names and their IQs
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
    dct={}
    for i in data:
        dct[i[0]]=int(i[1])
    return dct

def  rescue_people(smarties:dict, limit_iq:int):
    """
    return a list of people who can be rescued
    find out who would be saved in case of aliens invation 
    we have iq_limit of sum of iqs that can be on the ship
    return (how many trips i have to make, [[list of people i take with me on each trips]]) 
    i have to take as many people as I can as long as their iq sum isn't bigger then iq_limit 
    i have to take the smartest first
    # first i sort using quick sort function to find out the smartest and check whether adding their iq won't exceed iq_limit 
    # if there are two people with same iq I sould sort them in alphabetic order and then decide who to take
    >>> rescue_people({"Conan O'Brien": 160, 'Bill Gates':160}, 200)
    (2, [["Conan O\'Brien"], ['Bill Gates']])
    """
    if smarties=={}:
        return 0,[]
    # first i sort using quick sort function to find out the smartest and check whether adding their iq won't exceed iq_limit 
    #optimize the sorting
    # names=quick_sort(list(smarties.items()),1)
    names=sorted(list(smarties.items()), key=lambda x: x[1], reverse=True)
    p=names[0][1]
    i=1
    while i<len(names):
        j=i
        while (j<len(names))and(names[j][1]==p):
            j+=1
        # names[i:j]=quick_sort(names[i:j],0)
        # names[i:j]=sorted(names[i:j], key=lambda x: x[0])
        # reverse
        names[i:j]=sorted(names[i:j], key=lambda x: x[0])
        p=names[i][1]
        i=j
    res=[]
    amount=0
    while names:
        curent=0
        i=0
        res.append([])
        while names!=[] and i<len(names):
            if limit_iq-curent<0:
                break
            if limit_iq-curent>=names[i][1]:
                res[amount].append(names[i][0])
                curent+=names[i][1]
                names.remove(names[i])
                i-=1
            i+=1
        amount+=1
    return (amount, res)
@profile
def main():
    dct=read_file('week2\\Прибульці та IQ\\smart_people.txt')
    print(dct)
    res=rescue_people(dct, 200)
    print(res)
main()
print("--- %s seconds ---" % (time.time() - start_time))
