#Given a string s consisting of words and spaces, return the length of the last word in the string.
class LengthOfWord:
  def length_of_last_word(self, s: str) -> int:
    """
    Calculates the length of the last word in a string.

    Args:
        s: The input string.

    Returns:
        The length of the last word in the string.
    """

    result = 0
    # Start from the end of the string and iterate backwards
    for char in reversed(s):
      if char != ' ':
        result += 1
      # If a non-space character is found and result is already greater than 0,
      # we've found a word and can return the result
      elif result > 0:
        return result
    return result

# Create a single instance of LengthOfWord
length_of_word = LengthOfWord()

# Test cases
s = "Hello World"
results = length_of_word.length_of_last_word(s)
print(results)  # Output: 5

s = "   fly me   to   the moon  "
results = length_of_word.length_of_last_word(s)
print(results)  # Output: 4

s = "luffy is still joyboy"
results = length_of_word.length_of_last_word(s)
print(results)  # Output: 6
