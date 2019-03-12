
def score_domino_chain(chain):

# determines whether or not a chain of dominos is valid, then returns its score. a chain is valid if each pair of tiles 
# that are next to each other have the same number of dots on the sides that are touching. then, scores the chain 
# by summing all sides of a valid chain. invalid chains return a score of -1. 

  num_pieces = 0
  score = 0
  i = 1
  for x in chain: 
    num_pieces += 1
  
  if num_pieces > 0:                # score of first piece
    score += chain[0][0]+chain[0][1]
  
  while i < num_pieces: 
    if (chain[i-1][1]==chain[i][0]):
      #print("VALID")
      score += chain[i][0]+chain[i][1]
      i += 1
    else: 
      #print("INVALID")
      score = -1
      break

  return score


def add_domino(chain, new_tile):

# given a valid chain and an extra tile, adds new tile to chain if possible. new tile can be added to the front, back, or middle
# of the existing chain, and can be flipped. existing chain cannot be rearranged. returns new chain with tile added if possible, 
# or original chain if not.
 
  i = 0
  num_pieces = 0
  for x in chain: 
    num_pieces += 1
  
  if(new_tile[0] == new_tile[1]):     # new tile same on both sides, insert into valid chain
    while i < num_pieces:
      if (new_tile[0]==chain[i][0]):
        chain.insert(i, new_tile)
        break
      i+= 1
      
  if (new_tile[1] == chain[0][0]):    # new tile right side matches beginning of chain
    chain.insert(0, new_tile)
    
  elif (new_tile[0] == chain[0][0]):  # new tile left side matches beginning of chain
    reversed_tile = new_tile[::-1]    # flip tile, then insert
    chain.insert(0, reversed_tile)
    #print(chain)
    
  elif (new_tile[0] == chain[-1][1]): # new tile left matches end of chain
    chain.append(new_tile)
    #print(chain)

  elif (new_tile[1] == chain[-1][1]): # new tile right matches end of chain
    reversed_tile = new_tile[::-1]    # flip
    #print(reversed_tile)
    chain.append(reversed_tile)

  return chain
  
  
  def test_new_solution(input_chain, new_tile, expected_chain):
    original_chain = input_chain.copy()
    actual_score = add_domino(input_chain, new_tile)

    if (actual_score == expected_chain):
      return True

    print(f"""
             Input: {original_chain}
             New Tile: {new_tile}
    Expected Chain: {expected_chain}
      Actual Chain: {actual_score}""")

    return False
    
  
  def test_solution(input_chain, expected_score):
    actual_score = score_domino_chain(input_chain)

    if (actual_score == expected_score):
      return True

    print(f"""
             Input: {input_chain}
    Expected Score: {expected_score}
      Actual Score: {actual_score}""")

    return False
  
  def run_new_tests():
  test_cases = [
    {'input': [[1, 2], [2, 0]], 'new_tile' : [1, 3], 'expected_chain': [[3, 1], [1, 2], [2, 0]] },
    {'input': [[1, 2], [2, 0]], 'new_tile' : [3, 1], 'expected_chain': [[3, 1], [1, 2], [2, 0]] },
    {'input': [[1, 2], [2, 0]], 'new_tile' : [0, 3], 'expected_chain': [ [1, 2], [2, 0], [0, 3]] },
    {'input': [[1, 2], [2, 0]], 'new_tile' : [3, 0], 'expected_chain': [[1, 2], [2, 0], [0, 3]] },
    {'input': [[1, 3], [3, 0]], 'new_tile' : [3, 3], 'expected_chain': [[1, 3], [3, 3], [3, 0]] },
    {'input': [[1, 2], [2, 0]], 'new_tile' : [3, 3], 'expected_chain': [ [1, 2], [2, 0]] }
  ]
  num_tests = len(test_cases)
  num_failed = 0
  for test_case in test_cases:
    passed = test_new_solution(test_case['input'], test_case['new_tile'], test_case['expected_chain'])

    if passed == False:
      num_failed += 1

  if num_failed == 0:
    print(f"\n🎉 All {num_tests} test cases passed!")
  else:
    print(f"\n💥 Out of {num_tests} tests, {num_failed} failed")
#print("TESTING")
run_new_tests()


def run_tests():
  # These are the test cases we provide! Add your own test cases
  # to the end of this list to cover more edge cases.
  test_cases = [
    { 'input': [], 'expected_score': 0},
    { 'input': [[1, 2]], 'expected_score': 3},
    {'input': [[1, 2], [2, 0]], 'expected_score': 5 },
    {'input': [[1, 2], [2, 3], [3, 4], [5, 4]], 'expected_score': -1 },
    { 'input': [[2, 0], [2, 3]], 'expected_score': -1 }
  ]

  num_tests = len(test_cases)
  num_failed = 0

  for test_case in test_cases:
    passed = test_solution(test_case['input'], test_case['expected_score'])

    if passed == False:
      num_failed += 1

  if num_failed == 0:
    print(f"\n🎉 All {num_tests} test cases passed!")
  else:
    print(f"\n💥 Out of {num_tests} tests, {num_failed} failed")

run_tests()
