def main():
    names = ["Maria", "Diego", "Diego", "Jhon", "Paul", "Paul", "Paul"]
    hash_table = {}
    target = 7
    res = {}
    
    for n in names:
        if n in hash_table:
            hash_table[n] +=1
        else:
            hash_table[n] = 1
            
    for i,n in hash_table.items():
        print("Name: ",i, " apparences: ", n)
    
if __name__ == "__main__":
    main()