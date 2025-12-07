# synthetic_arc_generator.py
class ARCTaskGenerator:
    def generate_task(self):
        transform = random.choice([self.tile_pattern, self.symmetry_completion, self.color_substitution, self.shape_counting])
        train = [transform.apply(self.random_grid()) for _ in range(4)]
        test = [transform.apply(self.random_grid()) for _ in range(2)]
        return {"train": train, "test": test}
    
    def tile_pattern(self, grid):
        # E.g., repeat a 2x2 pattern to fill 6x6
        ...

for _ in range(100_000):
    task = ARCTaskGenerator().generate_task()
    save_to_jsonl(task)
