def WriteIn(filename, content):
    with open(filename, 'a') as f:
        f.write(content + '\n')
        f.close()

if __name__ =='__main__':
    filename = 'www.qwe.com.txt'
    content = 'qwe/qwe/asdfs.com'
    WriteIn(filename, content)