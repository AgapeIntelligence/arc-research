# augment.py
def augment_and_solve(input_grid):
    transforms = [
        lambda g: g,
        lambda g: rotate_90(g),
        lambda g: rotate_180(g),
        lambda g: rotate_270(g),
        lambda g: flip_horizontal(g),
        lambda g: flip_vertical(g),
    ]
    candidates = []
    for transform, inverse in zip(transforms, inverse_transforms):
        aug_input = transform(input_grid)
        aug_output = model.solve(aug_input)
        orig_output = inverse(aug_output)
        candidates.append(orig_output)
    return majority_vote(candidates)
