# Conway's Game of Life

---

## What is it?

This script simulates a state transition cycle across a dynamically sized 2D grid based on Conway's Game of Life. The matrix consists of coordinates that are either alive (`1`) or dead (`0`). Starting from a randomized setup, the entire board updates simultaneously generation by generation based on the density of surrounding live cells.

Simple neighborhood conditions dictate whether an individual element remains stable, changes state, or clears out.

---

## The Rules

Every coordinate evaluates its 8 immediate neighbors (horizontal, vertical, and diagonal) during each simulation cycle:

| Current State | Live Neighbors | Next State | Reason         |
|:-------------:|:--------------:|:----------:|:--------------:|
| Alive (`1`)   | < 2            | Dead       | Underpopulation|
| Alive (`1`)   | 2 or 3         | Alive      | Stability      |
| Alive (`1`)   | > 3            | Dead       | Overpopulation |
| Dead (`0`)    | exactly 3      | Alive      | Reproduction   |

---

## Features

- **Dynamic Geometry:** Automatically generates randomized rows (`n1`) and columns (`n2`) between 3 and 6.
- **Random Seeding:** Injects a randomized structural distribution of binary states (`0` and `1`) at startup.
- **Boundary Inclusion:** Full perimeter handling—edge and corner elements are fully evaluated against out-of-bounds safety constraints.
- **State Isolation:** Implements deep-copy buffering to prevent mid-iteration dataset corruption.

---

## How to Run

**Requirements:** Python 3.x (uses standard library modules `copy` and `random`)

```bash
python grid_transform.py
