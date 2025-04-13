# pagerank_algorithm_link_analysis

def pagerank(graph, damping_factor=0.85, max_iter=100, tol=1.0e-6):
    N = len(graph)
    pagerank = {page: 1.0 / N for page in graph}
    
    for _ in range(max_iter):
        new_pagerank = {}
        for page in graph:
            new_pagerank[page] = (1 - damping_factor) / N + damping_factor * sum(pagerank[other] / len(graph[other])
            for other in graph if page in graph[other])
        
        if sum(abs(new_pagerank[page] - pagerank[page]) for page in pagerank) < tol:
            break
        pagerank = new_pagerank
    
    return pagerank

# Example graph
graph = {'A': ['B', 'C'], 'B': ['C'], 'C': ['A']}
print(pagerank(graph))
