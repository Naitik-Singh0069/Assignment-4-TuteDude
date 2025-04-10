try:
    file=open('sample.txt','r')
    c=1
    for line in file:
        print('Line ',c,': ',line,end='')
    file.close()
except FileNotFoundError:
    print("File not found")