# grammar_constraints.py
from transformers import LogitsProcessor

class DSLConstraintProcessor(LogitsProcessor):
    def __init__(self, tokenizer, valid_operations):
        self.valid_ops = set(tokenizer.encode(op) for op in valid_operations)
    
    def __call__(self, input_ids, scores):
        valid_mask = self.get_valid_next_tokens(input_ids)
        scores[~valid_mask] = -float('inf')
        return scores

# Usage
valid_ops = ["rotate_90", "flip", "fill_color", "extend_pattern", ...]
processor = DSLConstraintProcessor(tokenizer, valid_ops)
output = model.generate(input_ids, logits_processor=[processor], max_new_tokens=256)
