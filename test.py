import sys

def count_to(n):
    for i in range(n):
        print(i)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print("Counting to %d" % n)
        count_to(n)