"""
1) Add the file and topic details.
   a) Mention the file name as `02-recursion.py`.
   b) Mention the topic as "Recursion and Recursive Time Complexity".
   c) Introduce recursion as a function calling itself.

2) Ask for the input value.
   a) Ask the user to enter a value for `n`.
   b) Suggest small values like 3 or 5.
   c) Convert the input into an integer.

3) Ask for a prediction.
   a) Ask how many times the countdown function will call itself.
   b) Include the chosen value of `n` in the question.
   c) Store the user's guess.

4) Create the recursive function.
   a) Define a function named `countdown(num)`.
   b) Print the current value of `num` each time the function runs.
   c) Use this print statement to show each recursive call.

5) Add the recursive condition.
   a) Check if `num` is greater than 0.
   b) Call `countdown(num - 1)` to move closer to the base case.
   c) Stop calling when `num` reaches 0.

6) Run the recursion.
   a) Pause before starting the countdown.
   b) Call `countdown(n)` using the user's number.
   c) Watch each recursive call print on the screen.

7) Show the time complexity.
   a) Print the total number of calls as `n + 1`.
   b) Display the user's original guess.
   c) Label the recursive countdown as `O(n)`.

8) Show how calls grow.
   a) Pause before showing larger examples.
   b) Use a for loop with values 5, 10, and 100.
   c) Print the number of calls as `size + 1`.
   d) Show that the number of calls grows linearly with `n`.
"""

# 02-recursion.py

# Topic: Recursion and Recursive Time Complexity

# A function that calls itself. Each call stacks up.

n = int(input("Enter n (try 3 or 5): "))
guess = input("How many times does countdown call itself for n = " + str(n) + "? ")
input("Recursion — watch each call. Press Enter to run ")

def countdown(num):

   print(" call — n =", num)

   if num > 0:

    countdown(num - 1)
   countdown(n)

print(" calls =", n + 1, " your guess:", guess, " -> O(n)")
input("Watch calls grow with n. Press Enter ")

for size in [5, 10, 100]:

 print(" n =", size, " calls =", size + 1, " -> O(n)")

