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
