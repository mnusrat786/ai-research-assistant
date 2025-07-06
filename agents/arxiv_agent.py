import arxiv

def search_arxiv(query, max_results=10):
    search = arxiv.Search(query=query, max_results=max_results)
    results = []
    for result in search.results():
        results.append(f"📘 {result.title}\n🔗 {result.pdf_url}\n")
    return "\n".join(results)
