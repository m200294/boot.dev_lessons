def tournament_rankings(names):
    results = []
    for index, name in enumerate(names):
        results.append(f"Rank: {index + 1}, Name: {name}")
    return results
