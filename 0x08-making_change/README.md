# Coin Change Problem - "Change Comes from Within"

## What I Did Today

Today, I tackled the **Coin Change Problem**! The challenge was simple to understand but tricky to solve: given a set of coin denominations and a target amount, I had to figure out the **minimum number of coins** needed to hit that exact amount. If it wasn't possible, I had to return `-1`. Seems easy, right? Well, it’s a bit more than just picking coins randomly!

### What I Learned

- **Greedy Algorithms**: The first approach I tried was the greedy method. I thought, "Just pick the biggest coin possible until I hit the amount." Turns out, this doesn’t always work — sometimes it gives the wrong result depending on the coin set!
  
- **Dynamic Programming**: Then, I explored dynamic programming. This technique breaks down the problem into smaller subproblems and stores solutions to avoid recalculating. It was a bit more complicated but guaranteed the right answer every time.

### Problem Example

```python
coins = [1, 2, 5]
amount = 11
# Result: 3 coins (5 + 5 + 1)
```

```python
coins = [2]
amount = 3
# Result: -1 (can't make 3 with only 2)
```

### Wrap-Up

I learned a ton about different algorithm strategies and how to choose the best one based on the problem constraints. It was fun trying different approaches and seeing where each one fails or succeeds. Now, I've got a great dynamic programming solution that works for any coin set.
