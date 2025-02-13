def check_has_all_indexes(numbers):
    size = len(numbers[1])
    check = {}
    
    for a in numbers:
        for i in range(1,size+1):
            check[i] = 0
        for b in a:
            if b in check:
                check[b]+=1
        for key, value in check.items():
            if value == 0:    
                return False    
    
    return True

def check_same_mixed_word(s1,s2):
    s1s1 = {}
    s2s2 = {}
    s1 = s1.upper()
    s2 = s2.upper()
    if len(s1) is not len(s2):
        return False
        
    for a in s1:
        if a in s1s1:
            s1s1[a]+=1
        else:
            s1s1[a] = 1
    for a in s2:
        if a in s1s1:
            if a in s2s2:
                s2s2[a]+=1
        else:
            return False
            
    return True        

def main():
    numbers = [
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4,6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    print(check_same_mixed_word("poma", "ampo"))
    
    
if __name__ == "__main__":
    main()