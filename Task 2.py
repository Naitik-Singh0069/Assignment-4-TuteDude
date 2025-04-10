'''Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''

with open('output.txt','a+') as file:
    user = input("Enter text to write to the file: ")
    file.write(user+"\n")
    user = input("\nEnter additional text to append: ")
    file.write(user)
    print("Data successfully appended.\nFinal content of output.txt:\n")
    file.seek(0)
    print(file.read())