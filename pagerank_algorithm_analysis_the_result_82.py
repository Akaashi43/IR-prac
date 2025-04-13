# pagerank_algorithm_analysis_the_result

def pagerank(graph, damping_factor=0.85, max_iter=100, tol=1.0e-6):
    N = len(graph)  
    pagerank = {page: 1.0 / N for page in graph} 
    for _ in range(max_iter):
        new_pagerank = {}
        for page in graph:
            rank_sum = sum(pagerank[other_page] / len(graph[other_page]) for other_page in graph if page in graph[other_page])
            new_pagerank[page] = (1 - damping_factor) / N + damping_factor * rank_sum
        if sum(abs(new_pagerank[page] - pagerank[page]) for page in pagerank) < tol:
            break
        
        pagerank = new_pagerank
    
    return pagerank
graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
}
pagerank_values = pagerank(graph)
print(pagerank_values)
