
# AI Lab Test 1 ⚙️

This repository contains solutions to three Artificial Intelligence
problems implemented using Python.

## Problems Included

### 1. Water Jug Problem

**Aim:** To measure a target amount of water using two jugs
of different capacities.

**Concepts Used:**
- State Space Search
- Breadth-First Search (BFS)
- Fill, Empty, and Pour Operations

**Input:** Jug A capacity, Jug B capacity, and target quantity.

**Output:** Steps performed to achieve the target quantity.

**File:** `water_jug.py`

### 2. Missionaries and Cannibals Problem

**Aim:** To transport three missionaries and three cannibals
across a river safely using a boat.

**Rules:**
- The boat can carry one or two people.
- Cannibals must not outnumber missionaries on either bank
  when missionaries are present.
- Everyone must cross the river safely.

**Concepts Used:**
- State Space Search
- Breadth-First Search (BFS)
- Valid State Checking

**Output:** The sequence of river crossings and the final state.

**File:** `missionaries_cannibals.py`

### 3. Sudoku Solver

**Aim:** To solve a 9x9 Sudoku puzzle using Python.

**Rules:**
- Each row must contain digits 1 to 9 without repetition.
- Each column must contain digits 1 to 9 without repetition.
- Each 3x3 subgrid must contain digits 1 to 9 without repetition.
- Zero represents an empty cell.

**Concepts Used:**
- Backtracking
- Recursion
- Constraint Checking

**Input:** A 9x9 Sudoku grid entered by the user.

**Output:** The solved Sudoku grid or a message if no solution exists.

**File:** `sudoku_solver.py`

## Technologies Used

- Python 3
- Visual Studio Code
- GitHub

## How to Run the Programs

Install Python 3 and open this repository in Visual Studio Code.

Run each program separately using the terminal.

### Water Jug Problem
```bash
python water_jug.py
```

### Missionaries and Cannibals Problem
```bash
python missionaries_cannibals.py
```

### Sudoku Solver
```bash
python sudoku_solver.py
```

## Project Structure

```text
AI-Lab-Test-1/
├── README.md
├── water_jug.py
├── missionaries_cannibals.py
└── sudoku_solver.py
```

## Conclusion

This project demonstrates basic Artificial Intelligence
problem-solving techniques using Python.

The Water Jug and Missionaries and Cannibals problems
demonstrate state-space search, while the Sudoku Solver
demonstrates backtracking and constraint checking.

## Author

Student Name: lalit solanki 
Roll no: Ic-2k23-54
Subject: Artificial Intelligence

Assessment: Lab Test 
