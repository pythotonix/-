"""dvv_mini_project.py"""
import copy


CAPACITY = {'Responsible AI': 25,
            'AI, Decision Making, and Society': 10,
            'Representation, Inference, and Reasoning in AI': 15}


PREREQUISITES = {
    'Responsible AI': {
        'Fundamentals of Programming': 40,
        'Linear Algebra': 30,
        'Probability and Statistics': 30},
    'AI, Decision Making, and Society': {
        'Worldview core': 40,
        'Decision Making': 40,
        'Fundamentals of Programming': 20},
    'Representation, Inference, and Reasoning in AI': {
        'Introduction to Algorithms': 40,
        'Probability and Statistics': 40,
        'Data Visualisation': 20}}


def read_file(filename):
    '''
    Reads file with registrations and
    return this information as a dictionary.
    'Number' is the ordinal number at the moment of registration.
    For our file, Robert Wilson was the first, and James Davis
    was the last (therefore, it has number 50).
    'Scores' are the scores of students for corresponding
    prerequisites.
    'Prioritization' is a prioritization of the corresponding students.
    >>> read_file('registrations.txt')['James Davis']
    {'Number': 50, 'Scores': {'Fundamentals of Programming': 70, \
'Linear Algebra': 63, 'Probability and Statistics': 71, 'Worldview core': 65, \
'Decision Making': 82, 'Introduction to Algorithms': 72, 'Data Visualisation': 93}, \
'Prioritization': {'AI, Decision Making, and Society': 1, \
'Representation, Inference, and Reasoning in AI': 2, 'Responsible AI': 3}}
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        main_dict = {}
        number = 0
        scores = {}
        prioritization = {}
        students_name = None
        for line in file:
            line = line.replace("- ", "")
            line = line.strip().split(': ')
            if "Prioritization" not in line[0] and "Name" not in line[0] and \
               "Date" not in line[0] and "Scores" not in line[0]:
                if len(line) > 1:
                    scores[line[0]] = int(line[1])
            if "Prioritization" in line[0]:
                element = line[1].strip().split("; ")
                prioritization = {i[3:]: int(i[0]) for i in element}
            if "Name" in line:
                if students_name is not None:
                    main_dict[students_name] = {
                        'Number': number,
                        'Scores': scores,
                        'Prioritization': dict(sorted(prioritization.items(), key=lambda item: item[1]))
                    }
                number += 1
                scores = {}
                students_name = line[1]
        if students_name is not None:
            main_dict[students_name] = {
                'Number': number,
                'Scores': scores,
                'Prioritization': dict(sorted(prioritization.items(), key=lambda item: item[1]))
            }
        return main_dict


def second_prior(result, registration_1, number_prior):
    """second prioritization"""
    result_1 = {key: [] for key in CAPACITY}

    for person_name, information in registration_1.items():
        for course, subjects in PREREQUISITES.items():
            if information['Prioritization'].get(course) == number_prior:
                subject_rate = sum(
    information['Scores'][subject] * (PREREQUISITES[course][subject] / 100)
    for subject in subjects
)
                person_inf = (person_name, round(subject_rate, 2), information['Number'] * (-1))
                result_1[course].append(person_inf)

    for course, persons in result_1.items():
        persons.sort(key=lambda x: (x[1], x[2]), reverse=True)
        result[course].extend(persons)

    return result

def registrated_deleter(result, courses, registration_1):
    """deletes registered students"""
    for course in courses:
        result[course] = result[course][:CAPACITY[course]]
        for person in result[course]:
            if person[0] in registration_1:
                del registration_1[person[0]]
    return result


def selection(registration):
    '''
    Makes a selection of students based on
    the registration information (please read the
    corresponding algorithm on CMS).
    Returns the dictionary, where the keys are subjects to choose
    and values are lists of tuples with students' name and ranking score
    sorted by ranking score in descending order.
    >>> selection(read_file('registrations.txt'))['Responsible AI']
    [('Robert Davis', 92.0), ('Linda Wilson', 91.6), \
('Patricia Williams', 89.5), ('Mary Brown', 85.8), \
('Robert Rodriguez', 85.3), ('William Wilson', 85.3), \
('Michael Davis', 83.4), ('Elizabeth Miller', 82.3), \
('Elizabeth Jones', 81.4), ('James Miller', 80.7), \
('Jennifer Johnson', 80.4), ('James Jones', 79.5), \
('Robert Williams', 79.3), ('John Williams', 77.3), \
('Mary Jones', 75.9), ('William Williams', 75.8), \
('Elizabeth Wilson', 74.0), ('Linda Johnson', 73.7), \
('Robert Miller', 71.5), ('Robert Wilson', 69.5), \
('William Rodriguez', 69.4), ('Jennifer Rodriguez', 69.0), \
('Patricia Johnson', 68.6), ('James Davis', 68.2), ('Jennifer Jones', 65.1)]
    '''
    registration_1 = copy.deepcopy(registration)
    result = {key: [] for key in CAPACITY}

    courses = list(result.keys())
    counter = 1
    while counter < 4:
        result = second_prior(result, registration_1, counter)
        counter += 1
        result = registrated_deleter(result, courses, registration_1)

    for key, value in result.items():
        result[key] = sorted(value, key=lambda x: (x[1], x[2]), reverse=True)

    for key, values in result.items():
        result[key] = [value[:-1] for value in values]

    return result
