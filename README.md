# AsiaCCS 2026: Privacy Evaluation Framework

## Reproducibility Package
This repository provides the dataset and processing tasks required to replicate the evaluation framework proposed in the poster.

## Step-by-Step Process (Tasks)
To replicate our results, execute the following tasks in order:

### Task 1: Environment Setup
Ensure Python 3.9+ is installed. Run the following to install dependencies:
`pip install -r requirements.txt`

### Task 2: Data Inspection
Navigate to `data/results.csv`. This dataset demonstrates the base-rate fallacy in Website Fingerprinting. Note the precision collapse from 0.94 (Closed) to 0.02 (Open).

### Task 3: Security Boundary Mapping
Run the mapping script to visualize the adversary dimensions:
`python3 scripts/radar_gen.py`

### Task 4: Sensitivity Analysis
Modify the `scores` array in `radar_gen.py` to reflect different adversary assumptions and observe how the security boundary (the blue area) expands or shrinks.

## Dataset Metadata
- **precision/recall**: Effectiveness of the attack.
- **fpr**: False Positive Rate (critical for "Open World" evaluations).
- **adversary_knowledge**: Mapping of Dimension A from the framework.

---
*Author names redacted for double-blind review.*