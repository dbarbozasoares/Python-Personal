
def getTuple():
    people = [
        ('Alice', 30),
        ('Bob', 25),
        ('Charlie', 35),
        ('David', 40),
        ('Eve', 22),
        ('Frank', 28),
        ('Grace', 32),
        ('Hannah', 24),
        ('Isaac', 29),
        ('Jack', 34),
        ('Karen', 27),
        ('Liam', 31),
        ('Mia', 33),
        ('Nathan', 26),
        ('Olivia', 38),
        ('Paul', 39),
        ('Quincy', 41),
        ('Rita', 23),
        ('Sam', 36),
        ('Tina', 37),
        ('Ursula', 42),
        ('Victor', 45),
        ('Wendy', 50),
        ('Xander', 33),
        ('Yara', 28),
        ('Zane', 26),
    ]
    return people

def getList():
    people = {
    'Alice': 30,
    'Bob': 25,
    'Charlie': 35,
    'David': 40,
    'Eve': 22,
    'Frank': 28,
    'Grace': 32,
    'Hannah': 24,
    'Isaac': 29,
    'Jack': 34,
    'Karen': 27,
    'Liam': 31,
    'Mia': 33,
    'Nathan': 26,
    'Olivia': 38,
    'Paul': 39,
    'Quincy': 41,
    'Rita': 23,
    'Sam': 36,
    'Tina': 37,
    'Ursula': 42,
    'Victor': 45,
    'Wendy': 50,
    'Xander': 33,
    'Yara': 28,
    'Zane': 26,
    }
    return people

def func(num):
    if num == 1:
        print("printing 1")
        return 1
    if num == 0:
        print("printing 0")
        return 0
    print("Running : ", num)
    i += 1
    num -= 1
    res = func(num)
    print("Analyzing: ", res)
    if res % 2 == 0:
        print("%2 == 0 : ", res*res)
        return res+res
    else:
        print("Result sum: ", res)
        return res+ res
    
def func2(number):
    if number == 0:
        return 0
    if number > 0:
        print(number)
        func2(number-1)
    else:
        func2(10)
        
def func3(string,a,b):
    if a >= b:
        print("False")
        return False
    if string[a] == string[b]:
        print("Exists")
        return True
    else:
        func3(string,a+1,b)

#T(n) = 1 + 1 + 1 * n 
#T(n) = 3 * n
#T(n) is O(n)    
def findPeopleUsingTuple(people, size):
    if size == 0:
        return
    else: #1
        if people[size][1] < 30:#1
            print(people[size]) 
    findPeople(people,size-1) # 1 * n
 
def findPeopleUsingHash(people, size):
    if size == 0:
        return
    else:
        name = list(people.keys())[size]
        age = people[name]
        if age < 30:
            print(name, people[name])
    findPeopleUsingHash(people, size-1)
 
def main():
    people = getList()
    findPeopleUsingHash(people, len(people)-1)
    
if __name__ == "__main__":
    main()
    
    
    
    
    
