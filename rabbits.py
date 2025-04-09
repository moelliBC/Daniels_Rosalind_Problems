def recurrence(n, k):
    #eingabe = input(nk)
   # liste = list(map(int, eingabe.split()))
    seq = [1, 1]
    for i in range(2, n):
        next_val = seq[i - 1] + seq[i - 2] * k
        seq.append(next_val)
    return seq

def solve_mortal_rabbits(n, m):
  """
  Calculates the number of rabbit pairs after n months,
  where each rabbit lives for m months. Uses an age-tracking approach.

  Args:
    n: The number of months (positive integer, problem constraint n <= 100).
    m: The lifespan of rabbits in months (positive integer, problem constraint m <= 20).

  Returns:
    The total number of rabbit pairs remaining after the n-th month.
  """

  # Initialize a list to store the number of rabbit pairs for each age.
  # ages[0] counts pairs aged 1 month (newborns)
  # ages[1] counts pairs aged 2 months
  # ...
  # ages[m-1] counts pairs aged m months (oldest possible)
  ages = [0] * m

  # Handle edge case n=0 if necessary, though problem implies n>=1
  if n == 0:
      return 0

  # Month 1: Start with one pair of newborn rabbits.
  ages[0] = 1

  # If n is 1, we are done.
  if n == 1:
      # Total pairs = sum of all ages
      return sum(ages) # Which is 1

  # Simulate months from 2 up to n
  # In each iteration 'month', we calculate the state at the *end* of that month.
  for month in range(2, n + 1):
      # --- Calculate state for the *end* of 'month' based on state at end of 'month-1' ---

      # 1. Calculate newborns for this month:
      #    Sum of pairs aged 2 to m months from the *previous* state (stored in 'ages').
      #    These are the pairs at indices 1 to m-1.
      newborns = sum(ages[i] for i in range(1, m))

      # 2. Age the population:
      #    Pairs that were age m (at ages[m-1]) die.
      #    Pairs that were age i (at ages[i-1]) become age i+1 (new ages[i]).
      #    We shift the counts down the list. It's safer to do this backwards
      #    to avoid overwriting values before they are used.
      for i in range(m - 1, 0, -1):
          ages[i] = ages[i - 1] # e.g., new 3-month-olds = old 2-month-olds

      # 3. Add the newborns (they are now 1 month old).
      ages[0] = newborns

  # After the loop (completing n months), return the total number of pairs.
  return sum(ages)



    #   --- You could also read input dynamically ---
    # try:
    #    line = input("Enter n and m separated by space: ").split()
    #    n_input = int(line[0])
    #    m_input = int(line[1])
    #      if n_input <= 0 or m_input <= 0 or n_input > 100 or m_input > 20:
    #         print("Please enter positive integers n (<=100) and m (<=20).")
    #    else:
    #        result = solve_mortal_rabbits(n_input, m_input)
    #        print(f"Result for n={n_input}, m={m_input}: {result}")
    # except (ValueError, IndexError):
    #    print("Invalid input. Please enter two integers separated by space.")
