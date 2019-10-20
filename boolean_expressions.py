"""
Boolean expressions evaluate to either True or False.

Examples:
* The expression "5 > 3" is evaluated as true.

*The expression "3 > 5" is evaluated as false.

 "5>=3" and "3<=5" are equivalent Boolean expressions,
 both of which are evaluated as true.

*"typeof true" returns "boolean" and "typeof false" returns "boolean"
Of course, most Boolean expressions will contain at least one variable
(x > 3), and often more (x > y).

"""

x = 5
y = 10
z = 14

# boolean expression type
print("Boolean exprressions  have type:", type(True), "\n")

# what values do you expect these will print?
print("x > y:", x > y,  "\n")
print("x < y:", x <= y,  "\n")
print("x == y:", x == y,  "\n")
print("x != y:", x != y,  "\n")

# inequalities can also be boolean expressions
print("x + y > z > x:", x + y > z > x,  "\n")







