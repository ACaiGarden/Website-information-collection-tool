#using IP
import nmap
import WriteInFile

class NmPortScanner():
    def __init__(self, ip_addr, filename):
        self.filename = filename        #保存的文件名
        self.ipaddress = ip_addr        #ip地址
        self.nm = nmap.PortScanner()    #初始化nmap

    def scan(self):
        '''
        端口扫描参数，可以在这里加入传入参数的函数。
        '''
        self.nm.scan(self.ipaddress, arguments='-F')


    def print_result(self):
        try:
            for x in self.nm[self.ipaddress]['tcp'].keys():
                message = str(x) + ': ' + str(self.nm[self.ipaddress]['tcp'][x]['state'])
                print(message)
                #print(x, ': ', self.nm[self.ipaddress]['tcp'][x]['state'])
                #filename = self.ipaddress + '.txt'
                WriteInFile.WriteIn(self.filename, message)
        except:
            pass



if __name__ == '__main__':
    try:
        s = NmPortScanner('183.232.231.172', 'filename.txt')
        s.scan()
        s.print_result()
    except:
        print("Port Scanner ERROR!")
