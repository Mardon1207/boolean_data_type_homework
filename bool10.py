def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    b=pow(a,1/2)
    b=int()
    return a-pow(b,2)==0
a=int(input())
print(main(a))