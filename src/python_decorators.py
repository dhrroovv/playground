# Approach 1
"""
def wrapper(func):
    print("before")
    print(func())
    print("after")


def main():
    return "hello world"

if __name__ == "__main__":
    wrapper(main)
"""

"""
Why cant we use this?
-> Its a basic function wrapping and not decoration
-> decorators need to return a `callable`
"""


# Approach 2
"""
def wrapper(f):
    def inner_wrap():
        print("before")
        print(f())  # replace this with just 'f' and notice the o/p
        print("after")

    return inner_wrap  # now the wrapper is returning a callable


def main():
    return "hello world"


if __name__ == "__main__":
    res = wrapper(main)
    res()
    res()
"""

"""
Approach 2 is similar to using functional programming! Right?
But why use decorations when we can use functional programming? Bcz:
    decorators provide better reproducibility and readability
"""


# Approach 3
"""
def wrapper(f):
    def inner_wrap():
        print("before")
        print(f())
        print("after")

    return inner_wrap


@wrapper  # use this for more pythonic way
def main():
    return "hello world"


if __name__ == "__main__":
    res = main()
"""

"""
Now its the real decoration and not a mere functional programming.
See how just writing @wrapper easily wraps our function with the wrapper.
"""


# Use functools.wrap(f) to preserve the actual function's metadata and docstring
