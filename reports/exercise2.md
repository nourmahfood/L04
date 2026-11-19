# Bug reports for exercise2.py

Line: 3
Problem: is_passing returns True for grade 5, but the docstring says "5 or more".
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password returns True for passwords with fewer than 8 characters, but the docstring says "at least 8 characters".
Example: is_valid_password("1234567") returns True, expected False.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: clamp returns low when x is less than low, but the docstring says "x, limited to the range from low to high", and the current implementation incorrectly uses min(x, low) which is always low or less.
Example: clamp(3, 5, 10) returns 5, which is correct, but clamp(2, 5, 10) returns 2, which is less than low, violating the range.
Fix: return max(low, min(x, high))
