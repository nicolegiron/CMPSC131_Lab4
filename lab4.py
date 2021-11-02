# Author: Nicole Giron nqg5259@psu.edu
# Collaborator: Khushal Mandavia kqm5921@psu.edu
# Collaborator: Srithulasi Nidamanuru sbn5256@psu.edu
# Collaborator:
# Section: 4
# Breakout: 6

def num_of_divisors(n):
  """
  given a positive int n, return number of divisors for n between 1-n inclusive
  You must use a while cond: style loop for this function.
  """
  count = 0
  num = n
  while (num > 0):
    if(n%num == 0):
      count += 1
    num-=1
  return count

def num_of_primes(n):
  """
  given a positive int n, return number of primes that is <= n.
  You must use num_of_divisors() function to help determine if a number is prime:
  a number is a prime if its number of divisors is 2.
  You must use a for... in range(...): style loop for this function.
  """
  count = 0
  for num in range(1, n+1):
    if(num_of_divisors(num) == 2):
      count += 1
  return count

def sum_n(n):
  """
  given a non-negative int n, return the sum 0+1+2+...+n
  You must use a while cond: style loop for this function.
  """
  sum = 0
  while(n > 0):
    sum += n
    n -= 1
  return sum

def print_n(s, n):
  """
  given a string s and a non-negative int n, print s n times
  you must use for ... in range(...): style loop for this function
  """
  for n in range(0, n):
    print(s)
  return

def run():
  num = int(input("Enter an int: "))
  print(f"sum is {sum_n(num)}.")
  print(f"{num} has {num_of_divisors(num)} divisors.")
  print(f"There are {num_of_primes(num)} primes <= {num}.")
  line = input("Enter a string: ")
  print_n(line, num)

if __name__ == "__main__":
  run()
