
def print_table(table):
    for person, data in table.items():
        print("Name: ", person, ", Information: ", data[0], data[1])
            
def find_value(table, target):
    for key,data in table.items():
        if key == target:
            print(f"Found: {key} with: {data}")
        if data:
            for info in data:
                if info == target:
                     print(f"Found: {key} with: {data}")
                     
def calculate_reward(table, word):
    res = {}
    total = 0
    for key, value in table.items():
        for letter in word:
            if letter in key:
                total += value
    print(f" The total is {total}")
    
def main():
    table = {'Diego': [25,"Yonge st"], 'Glenda':[26,"Bathrust st"], 'Maria': [28,"Yonge st"]}
    reward = {'a':3,'b':2,'c':1, 'd':-2}
    word = 'aacdf'
    calculate_reward(reward, word)
    run = True
    find_value(table, "Yonge st")
    # while run: 
        # name = input('Insert name:')
        # age = input('Insert age: ')
        # if age == "0":
            # run = False
        # address = input('Insert address: ')
        # table[name] = [age,address]
        # print_table(table)
    
if __name__ == "__main__":
    main()