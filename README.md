# Project 2: Deterministic QuickSelect

## Overview
This project implements the **Deterministic QuickSelect algorithm** using the **Median of Medians** approach to find the k-th smallest element (or median) of an array in **linear time**.  
---
## Files
- `deterministic.py` – Python implementation of Deterministic QuickSelect  
- `graph.png` – Graph comparing theoretical and experimental running times  
- `CSCS6212_PROJECT2_HETALLADD.docx` – Project report / documentation
---
## Requirements
- Python 3.x
- Standard libraries: `random`, `time`, `matplotlib` (if you want to plot results)
---
## How to Run
1. Clone the repository:
    ```bash
    git clone "https://github.com/HetalLad/CSCI6212_project2"
    ```
2. Run the Python script:
    ```bash
    python3 deterministic.py
    ```
3. The script will generate median values for different array sizes and output the experimental timings.
---
## Algorithm Description
The algorithm works as follows:
1. Divide the array into groups of 5 elements.
2. Sort each group using Insertion Sort and find the median.
3. Recursively find the median of medians, which is used as the pivot.
4. Partition the array into elements less than, equal to, and greater than the pivot.
5. Recur into the appropriate partition to find the k-th element.
**Time Complexity:**  
- Worst-case: \(O(n)\)  
- Best/Average case: \(O(n)\)
---
## Results
- Theoretical vs Experimental running times were compared and plotted.  
---

## Author
- Hetal Lad  

