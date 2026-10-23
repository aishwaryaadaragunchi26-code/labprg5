import sys

def simpleInt(pr, intr, time):
    return (pr * intr * time) / 100

if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time in years: "))

    si = simpleInt(p, r, t)
    print("Simple Interest =", si)
