
# Codeforces — A. Problem from Dolgoderevenskoye

**Platform:** Codeforces  
**Problem:** A. Problem from Dolgoderevenskoye  
**Language:** Python (PyPy 3)  
**Topic:** Number Theory, Game Theory, Mathematics  
**Difficulty:** A

---

## 1. Problem Overview

We are given a positive integer `n`.

For every positive divisor of `n`, there is exactly one card containing that divisor.

Two players, Artem and his opponent, play a game:

- Artem moves first and can remove any card.
- On every subsequent move, a player must remove a card whose parity is opposite to the previously removed card.
- If the previous card was even, the next player must remove an odd card.
- If the previous card was odd, the next player must remove an even card.
- A player who cannot make a move loses.

Both players play optimally.

Our task is to determine whether Artem wins.

---

## 2. Understanding the Problem

Instead of generating all divisors, we can solve the problem by comparing the number of odd and even divisors.

Every positive integer can be represented as:

\[
n = 2^k \times m
\]

where:
- `k` is the number of times 2 divides `n`.
- `m` is an odd number.

Let the number of divisors of `m` be `d`.

Then:

**Number of odd divisors:**

\[
d
\]

**Number of even divisors:**

\[
k \times d
\]

This gives us an important observation:

- If `k = 0`, all divisors are odd.
- If `k = 1`, the number of odd and even divisors is equal.
- If `k >= 2`, there are more even divisors than odd divisors.

---

## 3. Key Observation

Artem can choose the parity of the first card.

### Case 1: n is odd

All divisors are odd.

Artem removes one odd card. Since there are no even cards, the opponent cannot make a move.

**Result: YES**

### Case 2: n is divisible by 2 but not by 4

Here, `k = 1`.

The number of odd and even divisors is equal.

Whichever parity Artem chooses, the opponent can always respond. Artem eventually loses.

**Result: NO**

### Case 3: n is divisible by 4

Here, `k >= 2`.

There are more even divisors than odd divisors.

Artem can start by removing an even card and force the opponent to run out of valid moves first.

**Result: YES**

Therefore, the final condition is:

\[
\boxed{n \bmod 4 \neq 2}
\]

If `n % 4 == 2`, print `NO`.

Otherwise, print `YES`.

---

## 4. Solution Approach

We do not need to calculate or store the divisors.

For each test case:

1. Read `n`.
2. Check whether `n % 4 == 2`.
3. If true, print `NO`.
4. Otherwise, print `YES`.

---

## 5. Python (PyPy 3) Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())

    if n % 4 == 2:
        print("NO")
    else:
        print("YES")
```

---

## 6. Java Solution

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();

            if (n % 4 == 2) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
        }

        sc.close();
    }
}
```

---

## 7. Complexity Analysis

For each test case:

| Operation | Complexity |
|---|---|
| Read input | O(1) |
| Check divisibility by 4 | O(1) |
| Determine winner | O(1) |

**Time Complexity:** O(1) per test case.

**Auxiliary Space Complexity:** O(1).

---

## 8. Key Learnings

- Game theory problems do not always require simulating every move.
- Divisors can be classified based on parity.
- Prime factorisation can reveal the relationship between odd and even divisors.
- The first player's choice can determine the outcome of the game.
- A mathematical observation can reduce a seemingly complicated game to a simple modulo operation.

---

## 9. Final Approach

The entire solution comes down to one condition:

```python
if n % 4 == 2:
    print("NO")
else:
    print("YES")
```

No divisor generation, sorting, or game simulation is required.

**Final Complexity:** O(1) per test case.
