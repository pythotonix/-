'''Program for constructing a graph for the notes with which the given note \
is directly or indirectly related'''
import re
import os

import timeit
# from memory_profiler import profile


# build_graph_from_note(note_path, graph = None). Accepts the path to the file - the note note_path, for which you want to build a graph, and the optional parameter graph, in case we want to supplement the existing graph, which is a dictionary. This function returns a dictionary, where the keys are the names of the notes, and the value is a list of the names of the notes to which it is directly associated. If a note is not associated with anything, then its key should not be in the dictionary.
# For example, if you have the following files in the notes folder:

# note.md: linked to note4.md (A possible example of the content of the note.md file is: 'My favorite note is [[note4]].
# note1.md: linked to note.md
# note2.md: linked to note.md, note1.md, note3.md
# note3.md: not associated with anything
# note4.md: associated with note.md
# Then, when run, the build_graph_from_note("notes/note.md")function will return {"note": ["note4"], "note4": ["note"]}, because note.md is only linked to note4.md, and note4.md is linked to note.md. So it can't reach any other notes.
# Note that file extensions do not need to be written in the dictionary.


# The build_graph_from_note function is recursively building a graph dictionary from note files. Some optimizations we could make:

# Use a set instead of a list for the graph values. Checking if a link is already in the set would be faster than searching a list with list.index().
# Memoize the results of calling build_graph_from_note on each file path. We could use a cache dictionary to store the results, and check the cache before recursing, to avoid reprocessing files unnecessarily.
# Consider using multithreading to build the graph in parallel. The processing of each file is independent, so we could spawn threads to process groups of files concurrently.
# Use more efficient data structures for the final sorted graph, like an OrderedDict instead of a regular dict, to avoid the sorting step at the end.



# @profile
def build_graph_from_note(note_path: str, graph = None) -> dict:
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

# develop a convert_to_dot(graph) function whose parameter is the graph obtained using the first function build_graph_from_note, 
# and which saves the oriented graph corresponding to this dictionary to a file named graph.dot. An example of an oriented graph 
# can be seen here. It will allow you to quickly and efficiently visualize the graph and check if the other functions are working correctly.

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
#after optitmization, except that codewhisperer did not optimize anything

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