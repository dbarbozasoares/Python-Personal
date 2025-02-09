
i = 1
def func(num):
    global i
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
        
def main():
    name = "Doego"
    func3(name, 0,len(name)-1)
    
if __name__ == "__main__":
    main()