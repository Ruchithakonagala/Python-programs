a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
d=(b**2)-4*a*c
root1=(-b+(d**(0.5)))/2*a
root2=(-b-(d**(0.5)))/2*a
print(f"roots:({root1},{root2})")