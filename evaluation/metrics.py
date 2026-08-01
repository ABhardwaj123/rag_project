from vectorstore.store import query_collection


from vectorstore.store import query_collection

def hit_rate(test_set, collection, model, k):
    hits = 0
    total = len(test_set)
    detailed_results = []

    for item in test_set:
        question = item["question"]
        expected_ids = item["expected_ids"]

        query_embedding = model.encode(question).tolist()
        results = query_collection(collection, query_embedding, k)
        retrieved_ids = results['ids'][0]

        is_hit = bool(set(expected_ids).intersection(set(retrieved_ids)))
        if is_hit:
            hits += 1

        detailed_results.append({
            "question": question,
            "expected_ids": expected_ids,
            "retrieved_ids": retrieved_ids,
            "hit": is_hit
        })

    score = hits / total
    return score, detailed_results