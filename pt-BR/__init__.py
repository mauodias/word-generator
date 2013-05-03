def main():
    file = open('combinations.txt', 'w')
    a = []
    ab = []
    abc = []
    abcd = []
    
    for i in range(65, 91):
        a.append(chr(i))
        
    for i in a:
        for j in a:
            ab.append(i+j)
        for k in ab:
            abc.append(i+k)
        for l in abc:
            abcd.append(i+l)
            
    for i in ab+abc+abcd:
        file = open('combinations.txt', 'a')
        ans = raw_input('Is the combination ' + i + ' valid in portuguese? (Y/n)')
        if ans != 'n'.upper():
            file.write(i + '\n')
        file.close()

if __name__ == '__main__':
    main()
    
