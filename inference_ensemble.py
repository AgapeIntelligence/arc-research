from google.ai.gemini import GeminiClient
class EnsembleSolver:
    def __init__(self):
        self.client = GeminiClient(api_key="YOUR_API_KEY")

    def solve(self, input_grid, num_attempts=8):
        candidates = []
        for temp in [0.0, 0.3, 0.6, 0.9]:
            for seed in range(2):
                pred = self.client.generate_text(
                    input_grid,
                    temperature=temp,
                    do_sample=(temp > 0),
                    num_beams=4 if temp == 0 else 1
                )
                candidates.append(pred)
        return self.consensus_vote(candidates)

    def consensus_vote(self, candidates):
        from collections import Counter
        grids_as_tuples = [self.grid_to_tuple(c) for c in candidates]
        most_common = Counter(grids_as_tuples).most_common(1)[0][0]
        return self.tuple_to_grid(most_common)
