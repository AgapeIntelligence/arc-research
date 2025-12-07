# verifier.py
class TransformationVerifier:
    def verify_on_train_examples(self, task, predicted_program):
        """Test if the predicted transformation works on ALL training examples"""
        for train_case in task["train"]:
            try:
                result = self.execute_program(predicted_program, train_case["input"])
                if not grid_equal(result, train_case["output"]):
                    return False
            except:
                return False
        return True
    
    def solve_with_verification(self, task):
        for attempt in range(10):
            program = self.model.generate_program(task["train"])
            if self.verify_on_train_examples(task, program):
                return self.execute_program(program, task["test"][0]["input"])
        return self.model.solve_direct(task["test"][0]["input"])
