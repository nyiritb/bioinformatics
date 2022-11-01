from exercises.bioinformatics_stronghold.grph import overlaps

def max_overlap(a, b):
    for i in range(len(a)):
        if a[i:] == b[:len(a)-i]:
            return len(a)-i
    return 0

def overlap_graph(strings):
    edges = []
    for s1 in strings:
        for s2 in strings:
            if s1 != s2:
                overlap = max_overlap(s1, s2)
                edges.append((s1, s2, overlap))
    return edges

def merge_strings(a, b, overlap):
    return a + b[overlap:]
                
def shortest_common_superstring(strings):
    nodes = list(strings)
    edges = overlap_graph(strings)
    while len(nodes) > 1:
        edge_to_merge = max(edges, key=lambda x: x[2])
        if edge_to_merge[2] == 0:
            raise Exception('Graph is not a tree')
        nodes.remove(edge_to_merge[0])
        nodes.remove(edge_to_merge[1])
        nodes.append(merge_strings(*edge_to_merge))
        edges = overlap_graph(nodes)
    return nodes[0]


    