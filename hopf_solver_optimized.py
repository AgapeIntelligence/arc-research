import numpy as np
from typing import List, Any, Dict
from collections import Counter
from ethical_eval import ethical_score

class HopfAugmenter:
    def __init__(self, base_solver: Any, phases: int = 24):
        self.base = base_solver
        self.phases = phases

    def solve_task(self, task: dict) -> tuple[List[List[int]], Dict]:
        test_in = np.array(task["test"][0]["input"])
        q = self.to_quaternion(test_in)
        s2 = self.hopf_fibration(q).mean(axis=0)
        
        candidates = []
        s2_history = []
        
        for phase in np.linspace(0, 2*np.pi, self.phases, endpoint=False):
            lifted = self.inverse_hopf(s2, phase)
            pred = self.base.solve_with_hint(test_in, lifted.real)
            candidates.append(pred)
            s2_history.append(s2)
        
        consensus = self._consensus(candidates)
        ethics = ethical_score(task, candidates, s2_history)
        
        return consensus, ethics

    @staticmethod
    def to_quaternion(grid: List[List[int]]) -> np.ndarray:
        arr = np.array(grid, dtype=np.complex128).flatten()
        norm = np.linalg.norm(arr) or 1.0
        q = arr / norm
        pad = (-len(q)) % 4
        if pad: q = np.pad(q, (0, pad))
        return q.reshape(-1, 4)

    @staticmethod
    def hopf_fibration(q: np.ndarray) -> np.ndarray:
        a, b, c, d = q.T
        x = 2 * (a * np.conj(b) + c * np.conj(d))
        y = 2 * (a * np.conj(d) - b * np.conj(c))
        z = (np.abs(a)**2 + np.abs(b)**2 - np.abs(c)**2 - np.abs(d)**2)
        vec = np.stack([x.real, y.real, z.real], axis=-1)
        norm = np.linalg.norm(vec, axis=-1, keepdims=True)
        return np.where(norm > 0, vec / norm, vec)

    @staticmethod
    def inverse_hopf(s2_point: np.ndarray, phase: float = 0.0) -> np.ndarray:
        x, y, z = np.clip(s2_point, -1.0, 1.0)
        r = np.sqrt(np.clip((1 - z) / 2, 0, None))
        i = np.sqrt(np.clip((1 + z) / 2, 0, None))
        theta = np.arctan2(y, x) + phase
        return np.array([
            i * np.cos(theta / 2),
            r * np.sin(theta / 2),
            r * np.cos(theta / 2),
            i * np.sin(theta / 2)
        ], dtype=complex)

    @staticmethod
    def _consensus(grids: List[List[List[int]]]) -> List[List[int]]:
        tuples = [tuple(tuple(row) for row in g) for g in grids]
        best = Counter(tuples).most_common(1)[0][0]
        return [list(row) for row in best]
