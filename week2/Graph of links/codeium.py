'''Program for constructing a graph for the notes with which the given note \
is directly or indirectly related'''
import re
import os

import timeit
# from memory_profiler import profile

# @profile
def build_graph_from_note(note_path: str, graph=None) -> dict:
    '''
    This function returns a dictionary where keys are note names and values \
    are a list of note names to which it is directly related.
    '''
    if graph is None:
        graph = {}

    try:
        with open(note_path, 'r', encoding='UTF-8') as file:
            links = re.findall(r'\[\[([^\]]+)\]\]', file.read())
    except (FileNotFoundError, PermissionError) as e:
        print(e)
        return

    if links:
        note_name = os.path.basename(note_path).replace('.md', '')
        graph[note_name] = graph.get(note_name, set()).union(links)

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

    dot_graph = ['digraph {']
    dot_graph.extend([f'{note} -> {sub_note}' for note, sub_notes \
                      in graph.items() for sub_note in sub_notes])
    dot_graph.append('}')

    with open('graph.dot', 'w', encoding='UTF-8') as dot_file:
        dot_file.write('\n'.join(dot_graph))


#________________________________________________________________________________________
#after optitmization

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
# - build_graph_from_note: aprox. 0.36-0.38
# - convert_to_dot: aprox. 0.32-0.40

# build_graph_from_note(r"week2\Graph of links\note2.md")
# convert_to_dot(notes_dict)


#MEMORY PROFILE

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     11     48.5 MiB     48.5 MiB           5   @profile
#     12                                         def build_graph_from_note(note_path: str, graph=None) -> dict:
#     13     48.5 MiB      0.0 MiB           5       if graph is None:
#     14     48.5 MiB      0.0 MiB           1           graph = {}
#     15
#     16     48.5 MiB      0.0 MiB           5       try:
#     17     48.5 MiB      0.0 MiB          10           with open(note_path, 'r', encoding='UTF-8') as file:
#     18     48.5 MiB      0.0 MiB           5               links = re.findall(r'\[\[([^\]]+)\]\]', file.read())
#     19                                             except (FileNotFoundError, PermissionError) as e:
#     20                                                 print(e)
#     21                                                 return
#     22
#     23     48.5 MiB      0.0 MiB           5       if links:
#     24     48.5 MiB      0.0 MiB           4           note_name = os.path.basename(note_path).replace('.md', '')
#     25     48.5 MiB      0.0 MiB           4           graph[note_name] = graph.get(note_name, set()).union(links)
#     26
#     27     48.5 MiB      0.0 MiB          10           for link in links:
#     28     48.5 MiB      0.0 MiB           6               if link not in graph:
#     29     48.5 MiB      0.0 MiB           4                   build_graph_from_note(os.path.join(os.path.dirname(note_path), f'{link}.md'), graph)
#     30
#     31     48.5 MiB      0.0 MiB          33       graph = {note: sorted(sub_notes) for note, sub_notes in graph.items()}
#     32
#     33     48.5 MiB      0.0 MiB           5       return dict(sorted(graph.items()))


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     35     48.5 MiB     48.5 MiB           1   @profile
#     36                                         def convert_to_dot(graph: dict):
#     37                                             '''
#     38                                             This function saves the directed graph corresponding \
#     39                                             to the graph dictionary to a file named graph.dot.
#     40                                             '''
#     41     48.5 MiB      0.0 MiB           7       graph = {note: sorted(sub_notes) for note, sub_notes in graph.items()}
#     42     48.5 MiB      0.0 MiB           1       graph = dict(sorted(graph.items()))
#     43
#     44     48.5 MiB      0.0 MiB           1       dot_graph = ['digraph {']
#     45     48.5 MiB      0.0 MiB          24       dot_graph.extend([f'{note} -> {sub_note}' for note, sub_notes \
#     46     48.5 MiB      0.0 MiB          11                         in graph.items() for sub_note in sub_notes])
#     47     48.5 MiB      0.0 MiB           1       dot_graph.append('}')
#     48
#     49     48.5 MiB      0.0 MiB           2       with open('graph.dot', 'w', encoding='UTF-8') as dot_file:
#     50     48.5 MiB      0.0 MiB           1           dot_file.write('\n'.join(dot_graph))
