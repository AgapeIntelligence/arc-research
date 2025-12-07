# curriculum_learning.py
tasks_sorted = sorted(tasks, key=lambda t: difficulty_score(t))
phase1 = tasks_sorted[:200]   # Easy
phase2 = tasks_sorted[200:600] # Medium
phase3 = tasks_sorted[600:]    # Hard
for phase_data in [phase1, phase2, phase3]:
    trainer.train(phase_data)
