import sys
import random
import string

def main(args):
    length = int(args[1])
    print(f"=length: {length}")
    print(random_string(length))

def random_string(n):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))

if __name__ == "__main__":
    args = sys.argv
    try:
        main(args)
    except:
        print("Invalid args below")
        print(args)