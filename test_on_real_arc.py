# === 3C. Diverse Mock Tasks ==============================================

MOCK_TASKS = {
    "color_shift": {
        "input": [
            [0, 1, 2],
            [2, 1, 0],
            [1, 0, 2],
        ],
        "expected": [
            [1, 2, 0],
            [0, 2, 1],
            [2, 1, 0],
        ],
        "description": "Cycle all colors +1 mod 3."
    },

    "mirror_horizontal": {
        "input": [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ],
        "expected": [
            [4, 3, 2, 1],
            [8, 7, 6, 5],
        ],
        "description": "Horizontal mirror of each row."
    },

    "island_count": {
        "input": [
            [1, 0, 1, 1],
            [1, 0, 0, 1],
            [0, 0, 1, 0],
        ],
        "expected": 3,
        "description": "Count 4-connected nonzero islands."
    },

    "expand_cross": {
        "input": [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        "expected": [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0],
        ],
        "description": "Expand the cross outward around the center."
    },
}

