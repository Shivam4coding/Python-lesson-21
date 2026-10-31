"""
1) Add the file and topic details.
   a) Mention the file name as `01-binary-search.py`.
   b) Mention the topic as `O(log n)` and Binary Search.
   c) Introduce binary search as checking the middle and dropping half the list.

2) Create the sorted score list.
   a) Store the scores in a sorted list.
   b) Use this list for the binary search activity.

3) Ask the user to observe and predict.
   a) Display the list and its size.
   b) Ask the user to guess the maximum number of checks.
   c) Ask the user to pick a target number from the list.

4) Set up binary search.
   a) Create `low` to point to the first index.
   b) Create `high` to point to the last index.
   c) Create `steps` to count each check.

5) Use a while loop for searching.
   a) Repeat while `low` is less than or equal to `high`.
   b) Find the middle index using `(low + high) // 2`.
   c) Increase `steps` by 1.
   d) Print the value checked in each round.

6) Compare the middle value with the target.
   a) Stop the loop if the middle value matches the target.
   b) Move `low` to the right half if the middle value is smaller.
   c) Move `high` to the left half if the middle value is larger.

7) Display the search result.
   a) Print the target found.
   b) Print the position of the target.
   c) Print the number of steps taken.
   d) Show the user's guess.
   e) Label binary search as `O(log n)`.

8) Show slow step growth.
   a) Pause before showing larger input sizes.
   b) Print example max steps for n = 9, 100, and 1000.
   c) Highlight that binary search steps grow slowly as `n` increases.
"""

# 01-binary-search.py

# Topic: O(log n) and Binary Search

# Binary search always checks the middle and drops half the list.

scores = [1, 3, 5, 7, 9, 11, 13, 15, 17]

input("List: " + str(scores) + " n = 9 Press Enter ")
guess = input("Max checks to find any number in this list? ")
target = int(input("Pick a number from the list: "))

input("Binary search — checks the middle, drops half each round. Press Enter ")
low, high = 0, len(scores) - 1
steps = 0
while low <= high:
      mid = (low + high) // 2

      steps += 1
      print(" round", steps, "-> checked", scores[mid])
      if scores[mid] == target:

               break

      elif scores[mid] < target:
            low = mid + 1

      else:
            high = mid - 1

print(" found", target, "at position", mid + 1, "in", steps, "steps your guess:", guess, " -> O(log n)")
input("Steps grow slowly with n. Press Enter ")
for n, s in [(9, 4), (100, 7), (1000, 10)]:

 print(" n =", n, " max steps =", s, " -> O(log n)")