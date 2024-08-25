def is_palindrome(s):
    stack = []
    
    # Push all characters to the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack and compare with the original string
    for char in s:
        if char != stack.pop():
            return False
    
    return True

# Example usage
string = "racecar"
print(f"{string} is a palindrome: {is_palindrome(string)}")  # Output: True

string = "hello"
print(f"{string} is a palindrome: {is_palindrome(string)}")  # Output: False