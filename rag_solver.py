# rag_solver.py
def solve_with_rag(test_task):
    test_embedding = embed_task(test_task["train"])
    similar_tasks = vector_db.search(test_embedding, k=5)
    context = format_similar_tasks(similar_tasks)
    prompt = f"{context}\n\nNow solve:\n{test_task}"
    return model.generate(prompt)
