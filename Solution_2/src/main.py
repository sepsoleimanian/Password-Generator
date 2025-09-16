import random
import string
from typing import List, Optional
import nltk

nltk.download('words')
words = nltk.corpus.words.words()

def pin_gerenator(length: int = 8):
  return ''.join([random.choice(string.digits) for _ in range(length)])


def random_password_generator(length: int = 8, include_numbers: bool = True, include_symbols: bool = True):
  characters: str = string.ascii_letters
  if include_numbers:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation
  return ''.join([random.choice(characters) for _ in range(length)])

def memorable_password_generator(number_of_words: int = 4,
                                 seperator: str = '-',
                                 capitalization: bool = True,
                                 vocabulary: Optional[List[str]] = None) -> str:
  if vocabulary is None:
    if vocabulary is None:
      vocabulary = words
    else:
      vocabulary = vocabulary
      
  password_words = random.sample(vocabulary, number_of_words)
  
  if capitalization:
    password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
    
  return seperator.join(password_words)
  
if __name__ == '__main__':
  print(f'generated pin: {pin_gerenator()}\n'
      f'generated random password: {random_password_generator()}\n'
      f'generated memorable password: {memorable_password_generator()}')

  