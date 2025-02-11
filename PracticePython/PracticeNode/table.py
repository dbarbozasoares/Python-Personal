
def print_table(table):
    for person, data in table.items():
        print("Name: ", person, ", Information: ", data[0], data[1])
            
def main():
    table = {'Diego': [25,"Yonge st"], 'Glenda':[26,"Bathrust st"], 'Maria': [28,"Yonge st"]}
    run = True
    for key, data in table.items():
        if 'Yonge st' in data:
            print("found at: ", key)
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