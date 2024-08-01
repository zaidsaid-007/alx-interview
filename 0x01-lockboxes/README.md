[]: # Title: Lock boxes Project
[]: # Description: This project explores a problem-solving scenario involving lockboxes and keys, implemented
# Lockboxes Project

## Introduction
In this project, I explored a problem-solving scenario involving lockboxes and keys. The project is implemented in Python and helped me enhance my understanding of several fundamental concepts, including data structures and algorithms.

## Problem Description
I was given a set of `n` boxes, each numbered from 0 to n-1. Each box could contain keys to other boxes. The challenge was to determine if I could access all boxes starting from box 0, which is initially unlocked. A box could be opened if I had a key to it.

## Concepts I Learned

### Lists and List Manipulation
I learned how to work with lists, which are a fundamental data structure in Python. I used lists to:
- **Access Elements**: Check which keys are in a particular box.
- **Append/Remove Elements**: Manage the list of available keys and boxes to open.
- **Iterate**: Go through the list of keys or boxes efficiently.

### Graph Theory Basics
I realized that the problem could be represented as a directed graph, where:
- **Nodes**: Represent the boxes.
- **Edges**: Represent keys that could open other boxes.
- I explored graph traversal algorithms like Depth-First Search (DFS) and Breadth-First Search (BFS) to traverse the graph from the initial box.

### Algorithmic Complexity
Understanding time and space complexity became crucial. I learned that:
- **Time Complexity**: A solution visiting each box and key only once has a linear time complexity, O(n + m), where n is the number of boxes and m is the total number of keys.
- **Space Complexity**: Keeping track of visited boxes and available keys requires additional space, and understanding this helped in optimizing the solution.

### Recursion
I explored recursion to implement DFS. This approach involved functions calling themselves to explore all possible paths from the current box, which was a useful technique in navigating the problem space.

### Queue and Stack
- I used a **Queue** for BFS, which helped in exploring the nearest boxes first.
- A **Stack** was utilized for DFS, allowing me to explore as deep as possible along each branch before backtracking.

### Set Operations
I found sets useful for tracking visited boxes and available keys. Sets ensured no duplication and allowed efficient membership checks, which streamlined the process of managing which boxes had been accessed.

## Solution Overview
The solution involved a combination of the above concepts. I started by marking box 0 as opened and used its keys to open other boxes. Then, using a DFS or BFS approach, I continued to explore and open boxes, collecting more keys until all possible boxes were accessed.

## Setup and Usage

### Prerequisites
- Python 3.x

### Installation
To set up the project, I used the following commands:
```bash
git clone https://github.com/yourusername/lockboxes.git
cd lockboxes
```

### Running the Solution
To run the solution, I used:
```bash
python lockboxes.py
```

## Examples
### Example 1:
**Input**: `boxes = [[1], [2], [3], []]`  
**Output**: `True`

### Example 2:
**Input**: `boxes = [[1, 3], [3, 0, 1], [2], [0]]`  
**Output**: `False`

## Further Reading
For more information and resources, I found these links helpful:
- [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)
- [Graph Theory (Khan Academy)](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:graphing/x2f8bb11595b61c86:intro-to-graphs/a/graphs-article)
- [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-4-analysis-of-loops/)
- [Recursion (Real Python)](https://realpython.com/python-thinking-recursively/)

This README reflects my personal journey through the Lockboxes project, detailing the problem, the concepts I learned, and how I approached the solution.