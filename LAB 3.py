def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def to_lower_case(s):
    lower_case_string = ""
    for char in s:
        if 'A' <= char <= 'Z':
            lower_case_string += chr(ord(char) + 32)  
        else:
            lower_case_string += char
    return lower_case_string

def to_upper_case(s):
    upper_case_string = ""
    for char in s:
        if 'a' <= char <= 'z':
            upper_case_string += chr(ord(char) - 32)  
        else:
            upper_case_string += char
    return upper_case_string

def toggle_case(s):
    toggled_string = ""
    for char in s:
        if 'a' <= char <= 'z':
            toggled_string += chr(ord(char) - 32)  
        elif 'A' <= char <= 'Z':
            toggled_string += chr(ord(char) + 32)  
        else:
            toggled_string += char
    return toggled_string

def is_substring(s1, s2):
    return s1 in s2

def remove_string(main_string, remove_string):
    result = ""
    i = 0
    while i < len(main_string):
        if main_string[i:i+len(remove_string)] == remove_string:
            i += len(remove_string)  
        else:
            result += main_string[i]
            i += 1
    return result

def main():
    print("Select an operation:")
    print("1. Count vowels in a string")
    print("2. Convert string to lower case")
    print("3. Convert string to upper case")
    print("4. Toggle case of a string")
    print("5. Check if one string is in another")
    print("6. Remove one string from another")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        user_string = input("Enter a string: ")
        print("Number of vowels:", count_vowels(user_string))
    elif choice == 2:
        user_string = input("Enter a string: ")
        print("Lower case:", to_lower_case(user_string))
    elif choice == 3:
        user_string = input("Enter a string: ")
        print("Upper case:", to_upper_case(user_string))
    elif choice == 4:
        user_string = input("Enter a string: ")
        print("Toggled case:", toggle_case(user_string))
    elif choice == 5:
        string1 = input("Enter the first string: ")
        string2 = input("Enter the second string: ")
        if is_substring(string1, string2):
            print(f'"{string1}" is present in "{string2}".')
        else:
            print(f'"{string1}" is not present in "{string2}".')
    elif choice == 6:
        main_string = input("Enter the main string: ")
        remove_string_input = input("Enter the string to remove: ")
        result_string = remove_string(main_string, remove_string_input)
        print("Final string after removal:", result_string)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
