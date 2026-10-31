"""
1) Add the file and topic details.
   a) Mention the file name as `03-space-complexity.py`.
   b) Mention the topic as "Space Complexity and the Complexity Ladder".
   c) Introduce the program as a way to compare how different complexities grow.

2) Ask for a prediction.
   a) Ask how many steps `O(n^2)` takes when `n = 1000`.
   b) Store the user's guess.

3) Compare `O(n)` and `O(n^2)`.
   a) Pause before showing the growth examples.
   b) Use a for loop with values 10, 100, and 1000.
   c) Pause before each value of `n`.

4) Calculate growth values.
   a) Print `O(n)` as the same value as `n`.
   b) Print `O(n^2)` as `n * n`.
   c) Show that `O(n^2)` grows much faster than `O(n)`.

5) Show the user's guess.
   a) Print the original guess after the growth examples.
   b) Let the user compare the guess with the actual value.

6) Display the complexity ladder.
   a) Pause before showing the full ladder.
   b) Use `n = 1000` as the comparison size.
   c) Show `O(1)` as 1 step.
   d) Show `O(log n)` as 10 steps.
   e) Show `O(n)` as 1000 steps.
   f) Show `O(n^2)` as 1,000,000 steps.

7) Highlight the main idea.
   a) Explain that different complexities grow at different speeds.
   b) Show why choosing a better algorithm matters for large inputs.
"""

# 03-space-complexity.py

# Topic: Space Complexity and the Complexity Ladder

# Watch O(n) and O(n^2) grow, then see all four on the ladder.

guess = input("At n = 1000, O(n^2) takes how many steps? ")

input("Watch O(n) and O(n^2) grow. Press Enter ")

for n in [10, 100, 1000]:
    input("n = " + str(n) + " Press Enter ")

    print(" O(n) =", n, " O(n^2) =", n * n)

print(" your guess:", guess)

input("Full ladder at n = 1000. Press Enter ")

print(" O(1)=1 O(log n)=10 O(n)=1000 O(n^2)=1,000,000")
