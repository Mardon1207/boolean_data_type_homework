from math import trunc
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    b=trunc(pow(a,1/2))
    return a-pow(b,2)==0
a=int(input())
print(main(a))