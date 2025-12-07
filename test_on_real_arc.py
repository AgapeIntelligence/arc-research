# ===================================================================
# Section 3C: Mock Data Fallback (5 tasks for testing)
# ===================================================================

MOCK_TASKS = {
    "rotation": {"input": [[1, 0], [0, 1]], "output": [[0, 1], [1, 0]]},
    "flip": {"input": [[1, 1], [0, 0]], "output": [[0, 0], [1, 1]]},
    "pattern": {"input": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
                "output": [[1, 1, 1], [0, 1, 0], [1, 1, 1]]},
    "swap": {"input": [[2, 0], [0, 2]], "output": [[0, 2], [2, 0]]},
    "complex_swap": {"input": [[1, 2], [3, 4]], "output": [[4, 3], [2, 1]]},
}

tasks = [{"test": [MOCK_TASKS[key]]} for key in MOCK_TASKS]

print("Loaded mock tasks:", list(MOCK_TASKS.keys()))
"""
Section 4: Mock Base Solver (~71% accuracy)
"""
import numpy as np

class MockBaseSolver:
    def solve_with_hint(self, grid, hint):
        arr = np.array(grid)
        if np.random.rand() < 0.71:
            return arr.tolist()
        return np.rot90(arr, k=np.random.randint(1,4)).tolist()
"""
Section 5: Hopf-Augmented Solver Init
"""
from hopf_solver_optimized import HopfAugmenter
from ethical_eval import ethical_score

base_solver = MockBaseSolver()
hopf_solver = HopfAugmenter(base_solver, phases=12)
"""
Section 6: Evaluation Loop
"""
solved = 0
ethical_scores = []

for i, task in enumerate(tasks):
    try:
        pred, ethics = hopf_solver.solve_task(task)
        correct = any(np.array_equal(np.array(pred), np.array(test["output"]))
                      for test in task["test"])
        if correct:
            solved += 1
        ethical_scores.append(ethics["ethical_score"])
        print(f"{i+1}/{len(tasks)} | Task: {task['name']} | Solved: {solved} | Ethical: {ethics['ethical_score']:.3f}")
    except Exception as e:
        print(f"Task {task['name']} failed: {e}")
