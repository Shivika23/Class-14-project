with open('Sample_File.txt', 'r') as file:
    contents = file.read()
    print(contents)

with open('Sample_File.txt', 'w') as file:
    file.write("Hi, I'm Shivika, the class monitor of class 8.")

with open('Sample_File.txt', 'a') as file:
    file.write("\nMy favorite subject is Mathematics.")
    
file.close()