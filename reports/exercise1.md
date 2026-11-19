# Bug reports for exercise1.py

Line: 3
Problem: The condition checks if n % 2 == 1, which is true for odd numbers, not even numbers. For even numbers, n % 2 should equal 0.
Example: is_even(4) returns False, expected True
Fix: return n % 2 == 0

Line: 8
Problem: The function returns the sum of width and height, not the product, which is required for rectangle area.
Example: rectangle_area(5, 3) returns 8, expected 15
Fix: return width * height

Line: 13
Problem: The function adds 2 to n, but it should return twice the number (i.e., n multiplied by 2).
Example: double(4) returns 6, expected 8
Fix: return n * 2
