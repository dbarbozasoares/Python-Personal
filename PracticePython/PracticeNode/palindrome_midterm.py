def check_palindrome(string):
    helper = ""
    string = string.lower()
    if len(string) == 0 or len(string) == 1:
        return "Empty String"
    elif ((string[0]) and string[0] == " "):
        return "Remove extra spaces"
    else:
        if string[0] != string[len(string)-1]:
            return 'first is differnt than last'
        else:
            for i in range(len(string)):
                helper += string[len(string)-1-i]
            return helper == string

def check_palindrome_recursive(string, pos, helper):
    string = string.lower()
    if len(string) > 1:
        if string[0] == " " and string[len(string)-1] == " ":
            return "I cant compare spaces, please remove from start and end"
        if pos < 0:
            return helper == string
        else:
            helper += string[pos]
            return check_palindrome_recursive(string,pos-1, helper)  
        
def check_array_palindrome(array):
    helper = ""
    for word in array:
        print(f'{word}: {check_palindrome_recursive(word,len(word)-1, helper)}')
def main():
    strings = ["Glendinhag", "pop", "glass", "noon", " a", "pop"]
    check_array_palindrome(strings)
if __name__ == "__main__":
    main()