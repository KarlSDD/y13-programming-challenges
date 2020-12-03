# Programming challenges

## Task 1 - brute force hacking
A thief has managed to find out the four digits for an online PIN code, but doesn’t know the correct sequence needed to
hack into the account.

Design and write a program that appends all the possible combinations for any four numerical digits entered by the user.
The program should avoid displaying the same combination more than once.

## Task 2 - naming numbers
Show how to spell out a number in English. You can use a pre-existing implementation or make your own, but you should
support inputs up to at least one million.

## Task 3 - triangulate
Create a program that accepts 3 sides of a triangle.

It then works out if these sides form a triangle, and if so,
what type of triangle (e.g. Scalene, Isosceles, Right-Angle...)

Extension - Can you create an SVG of your triangle using Python to generate the file?

## Task 4 - name the day
Design a program to take 3 arguments, one for day, one for month and one for year.
Get your program to validate if this is an actual day, and, if it is, output the day of the week it is!

Hint: How do leap years affect this program?

## Task 5 - letters odd even
Even more Odd
Create a program that accepts a random list of integers and chars then puts them in order.

The rules for ordering are as follows - alphabetical for chars, small to large for integers - and then
all of the elements in the following order: characters, odd numbers, even numbers.

The return value will be your newly sorted list.

E.g. `[12, 17, 'a', 'h', 4, 1, 5, 'f', 8, 'z']` will become `['a', 'f', 'h', 'z', 1, 5, 17, 4, 8, 12]`

## Task 6 - email validator
Your task is to print a list containing only valid email addresses in alphabetical order.

Valid email addresses must follow these rules:

- It must have the username@websitename.extension format type.
- The username can only contain letters, digits, dashes and underscores.
- The website name can only have letters and digits.
