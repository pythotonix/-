'''Program for constructing a graph for the notes with which the given note \
is directly or indirectly related'''
import re
import os

import timeit
# from memory_profiler import profile

# @profile
def build_graph_from_note(note_path: str, graph = None) -> dict:
    '''
    This function returns a dictionary where keys are note names and values \
    are a list of note names to which it is directly related.
    '''
    if graph is None:
        graph = {}

    try:
        with open(note_path, 'r', encoding = 'UTF-8') as file:
            links = re.findall(r'\[\[([^\]]+)\]\]', file.read())
    except (FileNotFoundError, PermissionError) as e :
        print(e)
        return

    if links:
        try:
            graph[os.path.basename(note_path).replace('.md', '')] = links
        except KeyError:
            graph[os.path.basename(note_path).replace('.md', '')] += links

    for link in links:
        if link not in graph:
            build_graph_from_note(os.path.join(os.path.dirname(note_path), f'{link}.md'), graph)

    graph = {note: sorted(sub_notes) for note, sub_notes in graph.items()}

    return dict(sorted(graph.items()))

# @profile
def convert_to_dot(graph: dict):
    '''
    This function saves the directed graph corresponding \
    to the graph dictionary to a file named graph.dot.
    '''
    graph = {note: sorted(sub_notes) for note, sub_notes in graph.items()}
    graph = dict(sorted(graph.items()))

    with open('graph.dot', 'w', encoding = 'UTF-8') as dot_file:
        dot_file.write('digraph {\n')
        for note, sub_notes in graph.items():
            for sub_note in sub_notes:
                dot_file.write(f'{note} -> {sub_note}\n')
        dot_file.write('}')

#________________________________________________________________________________________
#before optitmization

#EXECUTION TIME
#Note: execution time is highly dependent on the machine running the script

build_graph_time = timeit.timeit(
    stmt='build_graph_from_note(r"week2\\Graph of links\\note2.md")',
    number=100,
    globals = globals()
)
print(f'Execution time of build_graph_from_note: {build_graph_time * 1000 / 100:.4f} milliseconds')


notes_dict = build_graph_from_note(r'week2\Graph of links\note2.md')
convert_to_dot_time = timeit.timeit(
    stmt='convert_to_dot(notes_dict)',
    number=100,
    globals = globals()
)
print(f'Execution time of convert_to_dot: {convert_to_dot_time * 1000 / 100:.4f} milliseconds')

# Execution time on mine machine:
# - build_graph_from_note: aprox. 0.40-0.42
# - convert_to_dot: aprox. 0.35-0.45


#MEMORY PROFILE

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#      9     49.0 MiB     49.0 MiB           1   @profile
#     10                                         def build_graph_from_note(note_path: str, graph = None) -> dict:
#     11                                             '''
#     12                                             This function returns a dictionary where keys are note names and values \
#     13                                             are a list of note names to which it is directly related.
#     14                                             '''
#     15     49.0 MiB      0.0 MiB           1       if graph is None:
#     16                                                 graph = {}
#     17
#     18     49.0 MiB      0.0 MiB           1       try:
#     19     49.0 MiB      0.0 MiB           2           with open(note_path, 'r', encoding = 'UTF-8') as file:
#     20     49.0 MiB      0.0 MiB           1               links = re.findall(r'\[\[([^\]]+)\]\]', file.read())
#     21                                             except (FileNotFoundError, PermissionError) as e :
#     22                                                 print(e)
#     23                                                 return
#     24
#     25     49.0 MiB      0.0 MiB           1       if links:
#     26                                                 try:
#     27                                                     graph[os.path.basename(note_path).replace('.md', '')] = links
#     28                                                 except KeyError:
#     29                                                     graph[os.path.basename(note_path).replace('.md', '')] += links
#     30
#     31     49.0 MiB      0.0 MiB           1       for link in links:
#     32                                                 if link not in graph:
#     33                                                     build_graph_from_note(os.path.join(os.path.dirname(note_path), f'{link}.md'), graph)   
#     34
#     35     49.0 MiB      0.0 MiB           7       graph = {note: sorted(sub_notes) for note, sub_notes in graph.items()}
#     36
#     37     49.0 MiB      0.0 MiB           1       return dict(sorted(graph.items()))


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     39     49.0 MiB     49.0 MiB           1   @profile
#     40                                         def convert_to_dot(graph: dict):
#     41                                             '''
#     42                                             This function saves the directed graph corresponding \
#     43                                             to the graph dictionary to a file named graph.dot.
#     44                                             '''
#     45     49.0 MiB      0.0 MiB           7       graph = {note: sorted(sub_notes) for note, sub_notes in graph.items()}
#     46     49.0 MiB      0.0 MiB           1       graph = dict(sorted(graph.items()))
#     47
#     48     49.0 MiB      0.0 MiB           2       with open('graph.dot', 'w', encoding = 'UTF-8') as dot_file:
#     49     49.0 MiB      0.0 MiB           1           dot_file.write('digraph {\n')
#     50     49.0 MiB      0.0 MiB           5           for note, sub_notes in graph.items():
#     51     49.0 MiB      0.0 MiB          10               for sub_note in sub_notes:
#     52     49.0 MiB      0.0 MiB           6                   dot_file.write(f'{note} -> {sub_note}\n')
#     53     49.0 MiB      0.0 MiB           1           dot_file.write('}')
