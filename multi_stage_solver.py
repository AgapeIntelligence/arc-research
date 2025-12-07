# multi_stage_solver.py
class StagedSolver:
    def solve(self, task):
        transform_type = self.classify_transform(task["train"])
        if transform_type == "symmetry":
            axis = self.detect_symmetry_axis(task["train"])
            center = self.find_symmetry_center(task["train"])
        solver = self.get_specialist_solver(transform_type)
        return solver.solve(task["test"][0]["input"], params)
