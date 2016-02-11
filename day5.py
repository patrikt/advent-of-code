import csv

def vowels(word):
  # 'word' contains at least three vowels (aeiou only),
  # like aei, xazegov, or aeiouaeiouaeiou.
  vowels = 'aeiou'
  return sum(c in vowels for c in word)

def double_letters(word):
  # 'word' contains at least one letter that appears twice
  # in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc,
  # or dd).
  res = []
  for i in range(len(word)-1):
    if word[i] == word[i+1]:
      res.append(word[i]*2)
  return len(res)

def cant_contain(word):
  # 'word' does not contain the strings ab, cd, pq, or xy,
  # even if they are part of one of the other requirements.
  bad_words = ['ab','cd','pq','xy']
  res = []
  for t in bad_words:
    res.append(t in word)
  return sum(res)

def nice_string(word):
  if (vowels(word) >= 3) & (double_letters(word) > 0) & (cant_contain(word) < 1):
    return True
  return False

if __name__ == '__main__':
  res = []
  with open('data/day5.txt', 'rb') as csvfile:
    words = csv.reader(csvfile)
    for word in words:
      res.append(nice_string(word[0]))
  print sum(res)