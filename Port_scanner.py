import nmap
import WriteInFile

class NmPortScanner():
    def __init__(self, ip_addr):
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
                filename = self.ipaddress + '.txt'
                WriteInFile.WriteIn(filename, message)
        except:
            pass

if __name__ == '__main__':
    s = NmPortScanner('180.97.83.149')
    s.scan()
    s.print_result()

'''
host = 'www.china-qimei.com'
ip_addr = socket.getaddrinfo(host, 'http')
print(ip_addr[0][4][0])

nm=nmap.PortScanner()
nm.scan('127.0.0.1',  arguments='-F')
print(nm.command_line())
print(nm['127.0.0.1']['tcp'].keys())

for x in nm['127.0.0.1']['tcp'].keys():
    print(x, ': ', nm['127.0.0.1']['tcp'][x]['state'])

'''