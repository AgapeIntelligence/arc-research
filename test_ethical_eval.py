"""
test_ethical_eval.py — Validation of ethical_eval.py
----------------------------------------------------
Runs the ethical evaluation suite on a real-style ARC task
with Hopf-Augmented predictions.
"""

import numpy as np
from ethical_eval import ethical_score

# Sample ARC-style symmetry task
sample_task = {
    "train": [
        {"input": [[1, 0], [0, 1]], "output": [[1, 0], [0, 1]]},
        {"input": [[0, 1], [1, 0]], "output": [[0, 1], [1, 0]]},
    ],
    "test": [{"input": [[1, 0, 0], [0, 0, 1], [0, 1, 0]]}]
}

# Simulated Hopf-Augmented predictions (12–24 phases)
candidates = [
    [[1, 0, 0], [0, 0, 1], [0, 1, 0]],  # correct
    [[1, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 0, 1], [0, 1, 0], [1, 0, 0]],  # rot90
    [[1, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 1, 0], [1, 0, 0], [0, 0, 1]],  # rot180
    [[0, 0, 1], [1, 0, 0], [0, 1, 0]],  # rot270
] * 2  # simulate 12 candidates

# Simulated S² history (12 phases)
s2_history = [
    np.array([0.8, 0.1, -0.58]),
    np.array([0.79, 0.12, -0.59]),
    np.array([0.81, 0.09, -0.57]),
] * 4

# Run ethical evaluation
result = ethical_score(sample_task, candidates, s2_history)

print("Ethical Evaluation Results:")
print(f"  Ethical Score:      {result['ethical_score']:.3f}")
print(f"  Coherence:          {result['coherence']:.3f}")
print(f"  Symmetry Bias:      {result['symmetry_bias']:.3f}")
print(f"  Fiber Coverage:     {result['fiber_coverage']:.3f}")
print(f"  Safe for Use:       {result['safe']}")
