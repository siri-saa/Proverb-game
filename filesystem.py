import random

def guess_proverb(file_name):
  """Guesses a proverb from a file.

  Args:
    file_name: The name of the file containing the proverbs.

  Returns:
    The proverb that was guessed.
  """

  with open(file_name, 'r') as f:
    proverbs = f.readlines()

  # Choose a random proverb.
  random_proverb = random.choice(proverbs)

  # Ask the user to guess the proverb.
  guess = input('What is the proverb? ')

  # Check if the user guessed correctly.
  if guess == random_proverb:
    print('Correct!')
  else:
    print('Incorrect. The correct proverb is:', random_proverb)

if __name__ == '__main__':
  file_name = 'proverbs.txt'
  guess_proverb(file_name)
