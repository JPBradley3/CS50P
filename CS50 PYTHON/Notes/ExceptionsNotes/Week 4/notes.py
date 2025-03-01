## Make your own library
## This is when there is a lot of workflow that repeats itself
##

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

## This line is for telling python that the code is ending even if the user has entered nothing. Its a ending loop.
if __name__ == "__main__":
main()
