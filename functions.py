def say_hi(name):
    print("Hello", name)

say_hi('Jose')

def keyword_arguments(name, **kwargs):
    print(f"Hello {name}")
    print(kwargs['one'])

keyword_arguments("Alpha", one=1, two=2)


def return_func():
    return 5
print(return_func())