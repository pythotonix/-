'''Program to find out in what order the aliens will deliver the chosen people to their planet'''


def read_file(file_path: str) -> dict:
    '''
    Reads a file and returns a dictionary, the keys of which should be the names of people, \
    and the values - their IQ level.

    >>> read_file('smart_people.txt')
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, 'Marilyn vos Savant': 186, \
'Judith Polgar': 170, 'Quentin Tarantino': 163, 'Bill Gates': 160, "Conan O'Brien": 160, \
'Emma Watson': 132, 'Barack Obama': 137}
    '''
    smarties = {}
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file:
            if line[0].isalpha():
                name = line.split(',')[0]
                iq = int(line.split(',')[1])
                smarties[name] = iq
    return smarties

# def rescue_people(smarties: dict, limit_iq: int) -> tuple:
#     '''
#     Returns a tuple of the number of required trips and a list of lists, \
#     where each inner list represents a trip and contains the names of people \
#     who are transported on this trip and whose iq sum must not exceed the given iq limit.

#     >>> rescue_people({'Steve Jobs': 160, 'Albert Einstein': 160, \
# 'Sir Isaac Newton': 195, 'Nikola Tesla': 189}, 500)
#     (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
#     >>> rescue_people({}, 500)
#     (0, [])
#     '''
#     smarties = dict(sorted(smarties.items(), key=lambda x: (-x[1], x[0])))

#     iq_sum = 0
#     trip = []
#     all_trips = []
#     for person, iq in smarties.items():
#         if iq_sum + iq <= limit_iq:
#             trip += [person]
#             iq_sum += iq
#         else:
#             if trip:
#                 all_trips += [trip]
#                 trip = [person]
#                 iq_sum = iq
#     if trip:
#         all_trips += [trip]
#     return (len(all_trips), all_trips)


def list_element_del(lst: list[tuple], to_del: str) -> list[tuple]:
    """
    (list[tuple], str) -> list[tuple]
    The function delete element which include to_del
    >>> list_element_del([("a", 1), ("b", 1), ("c", 1)], "a")
    [('b', 1), ('c', 1)]
    """
    for i, element in enumerate(lst):
        if element[0] == to_del:
            lst.pop(i)
    return lst


def selection_sort_dict(dct: dict) -> list[tuple]:
    """
    (list[tuple]) -> list[tuple]
    The function use selection sort algorithm
    to sort list of tiples with names.
    >>> selection_sort_dict({"Steve Jobs": 160, \
"Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189})
    [('Steve Jobs', 160), ('Albert Einstein', 160), ('Nikola Tesla', 189), \
('Sir Isaac Newton', 195)]
    """
    tuple_list = [tuple([key, value]) for key, value in dct.items()]
    for i, element in enumerate(tuple_list):
        min_i = i
        for j in range(i+1, len(tuple_list)):
            if tuple_list[min_i][1] > tuple_list[j][1]:
                min_i = j
        tuple_list[i], tuple_list[min_i] = tuple_list[min_i], element
    return tuple_list


def selection_sort_list_tuple(tuple_list: dict) -> list[tuple]:
    """
    (list[tuple]) -> list[tuple]
    The function use selection sort algorithm
    to sort list of tiples with names.
    >>> selection_sort_list_tuple([('Steve Jobs', 160), ('Albert Einstein', 160), \
('Nikola Tesla', 189), ('Sir Isaac Newton', 195)])
    [('Steve Jobs', 160), ('Albert Einstein', 160), \
('Nikola Tesla', 189), ('Sir Isaac Newton', 195)]
    >>> selection_sort_list_tuple([('M', 160), ('A', 160), ('W', 189), ('P', 195)])
    [('M', 160), ('A', 160), ('W', 189), ('P', 195)]
    """
    for i, element in enumerate(tuple_list):
        min_i = i
        # порівнюю з eлементами з правої частини списку
        for j in range(i+1, len(tuple_list)):
            if (tuple_list[min_i][0] < tuple_list[j][0]) and (
                    tuple_list[min_i][1] == tuple_list[j][1]):min_i = j
        tuple_list[i], tuple_list[min_i] = tuple_list[min_i], element
    return tuple_list


def rescue_people(smarties: dict, limit_iq: int):
    """
    The function
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
"Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
"Sir Isaac Newton": 195, "Nikola Tesla": 189}, 250)
    (4, [['Sir Isaac Newton'], ['Nikola Tesla'], ['Albert Einstein'], ['Steve Jobs']])
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
"Sir Isaac Newton": 195, "Nikola Tesla": 189}, 2000)
    (1, [['Sir Isaac Newton', 'Nikola Tesla', 'Albert Einstein', 'Steve Jobs']])
    >>> rescue_people({}, 400)
    (0, [])
    """
    if smarties == {}:
        return (0, [])
    trip_counter = []
    sorted_smarties_list = selection_sort_list_tuple(selection_sort_dict(smarties))
    limit_iq_counter = limit_iq
    if sorted_smarties_list[-1][1] > limit_iq:
        return (0, [])
    while len(sorted_smarties_list) >= 1:
        trip = [limit_iq_counter]
        for smart in reversed(sorted_smarties_list):
            if smart[1] > 130 and trip[0] - smart[1] >= 0:
                trip[0] -= smart[1]
                trip.append(smart[0])
                sorted_smarties_list = list_element_del(sorted_smarties_list, smart[0])
        trip_counter.append(trip)
    result_list = [trip_[1:] for trip_ in trip_counter]
    result = (len(result_list), result_list)
    return result
