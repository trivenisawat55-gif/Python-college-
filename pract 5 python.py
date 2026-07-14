#function to find the Frequency of a character in a string
def find_frequency(string,char):
    return string.count(char)
#function to replace a character by another character in a string
def replace_character(string,old_char,new_char):
    return string.replace(old_char,new_char)
#function to remove the first occurence of character from the string
def remove_first_occurence(string,char):
    return string.replace(char,'',1)
#function to remove all occurence of character from the string
def remove_all_occurence(string,char):
    return string.replace(char,'')
#main function to drive the menu and operations
def menu():
    while True:
        print("\nMenu")
        print("1.Find the Frequency of a character in a string")
        print("2.Replace a character by another character")
        print("3.Remove the first occurence of character from the string")
        print("4.Remove all occurence of character from the string")
        print("5.Exit")
        choice=input("Enter your choice :-[1-5]")
        if choice == '1':
            string=input("Enter the string")
            char=input("enter the character to find frequency")
            print(f"The frequency of {char} in the {string} is:{find_frequency(string,char)}")
        elif choice == '2':
            string=input("Enter the string")
            old_char=input("Enter the character to replace")
            new_char=input("Enter the new character")
            print(f"Updated string: {replace_character(string,old_char,new_char)} ")
        elif choice == '3':
            string=input("Enter the string")
            char=input("Enter the character to remove first occurence")
            print(f"Updated string: {remove_first_occurence(string,char)}")
        elif choice == '4':
            string=input("Enter the string")
            char=input("Enter the character to remove all occurence")
            print(f"Updated string: {remove_all_occurence(string,char)}")
        elif choice == '5':
            print("Exiting the program")
            break
        else:
            print("Invalid choice! Please Enter a valid option [1-5]")
            
            
        
#run the menu function
menu()
