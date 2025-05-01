import random

def oe_list():
    o = [1, 3, 5, 7, 9]  
    e = [2, 4, 6, 8]     
    
    print("Original odd integers:", o)
    print("Original even integers:", e)

    o[2] = e
    print("Odd integers after replacement:", o)

    o = o[:2]+e+o[3:]  
    o.sort()
    print("Flattened and sorted list:", o)

def occ():
    nums = [10, 23, 45, 10, 67, 23, 89, 10, 34, 56, 10, 78, 90, 10, 23, 45, 67, 89, 10, 12]
    print("List:", nums)
    u_num = int(input("Enter a number to find its positions: "))
    posi = []
    
    for i in range(len(nums)):
        if nums[i] == u_num:
            posi.append(i)

    if posi:
        print("Positions of", u_num, "in the list:", pos)
    else:
        print(u_num, "is not in the list.")
    
def dup():
    r = [random.randint(1, 30) for _ in range(50)]
    print("random numbers:", r)
    u = list(set(r))
    print("new numbers after removing duplicates:", u)

def posneg():
    r = [random.randint(-30, 30) for _ in range(30)]
    print("random numbers:", r)
    p = [n for n in r if n > 0]
    n = [n for n in r if n < 0]
    print("Positive numbers:", p)
    print("Negative numbers:", n)

def strup():
    strings = ["aditya", "dalal", "is", "a", "cool guy"]
    print("Original List:", strings)
    
    upper_strings = [s.upper() for s in strings]
    
    print("Uppercase List:", upper_strings)

def convtemp():
    f = [random.randint(32, 212) for _ in range(10)]
    print("Fahrenheit temperatures:", f)
    c = [(t - 32) * 5 / 9 for t in f]
    print("Celsius temperatures:", c)

def stackdat():
    s = []
    while True:
        print("\nStack Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        c = int(input("Enter your choice: "))
        if c == 1:
            i = input("Enter item to push: ")
            s.append(i)
            print(f"{i} pushed to stack.")
        elif c == 2:
            if s:
                p = s.pop()
                print(f"{p} popped from stack.")
            else:
                print("Stack is empty.")
        elif c == 3:
            print("Current stack:", s)
        elif c == 4:
            break
        else:
            print("Invalid choice.")

def queuedat():
    q = []
    while True:
        print("\nQueue Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        c = int(input("Enter your choice: "))
        if c == 1:
            i = input("Enter item to enqueue: ")
            q.append(i)
            print(f"{i} enqueued to queue.")
        elif c == 2:
            if q:
                d = q.pop(0)
                print(f"{d} dequeued from queue.")
            else:
                print("Queue is empty.")
        elif c == 3:
            print("Current queue:", q)
        elif c == 4:
            break
        else:
            print("Invalid choice.")

def listcomp():
    l1 = [random.randint(1, 20) for _ in range(10)]
    l2 = [random.randint(1, 20) for _ in range(5)]
    print("List 1:", l1)
    print("List 2:", l2)
    d = [n for n in l1 if n not in l2]
    print("Numbers in List 1 not in List 2:", d)

def main():
    print("Select a task:")
    print("1. Modify and sort lists")
    print("2. Find occurrences of a number")
    print("3. Remove duplicates from a list")
    print("4. Split positive and negative numbers")
    print("5. Convert strings to uppercase")
    print("6. Convert Fahrenheit to Celsius")
    print("7. Stack operations")
    print("8. Queue operations")
    print("9. List difference")

    c = int(input("Enter your choice (1-9): "))

    if c == 1:
        oe_list()
    elif c == 2:
        occ()
    elif c == 3:
        dup()
    elif c == 4:
        posneg()
    elif c == 5:
        strup()
    elif c == 6:
        convtemp()
    elif c == 7:
        stackdat()
    elif c == 8:
        queuedat()
    elif c == 9:
        listcomp()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
