import sys

def simpleInt(pr, intr, time):
    return (pr * intr * time) / 100

if __name__ == "__main__":
    principal = sys.argv[1]
    interest = sys.argv[2]
    time = sys.argv[3]

    si = simpleInt(p, r, t)
    print("Simple Interest =", si)
