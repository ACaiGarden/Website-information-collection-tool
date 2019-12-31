import socket
from Port_scanner import NmPortScanner
from Burp_force_directory import Dir_Scanner
class main():
    def __init__(self):
        self.domain = ''                            #目标网址
        self.ipaddress = self.get_domain_to_ip()    #由目标网址得到的IP地址
        self.get_port()                             #调用端口扫描函数
        self.get_dir()                              #调用目录扫描函数

    def get_domain_to_ip(self):
        self.domain = input("Please input the domain(Without 'http://'):")
        '''
        这里往后可以加正则表达式
        '''
        try:
            ip_addr = socket.getaddrinfo(self.domain, 'http')
            print(ip_addr[0][4][0])
            return ip_addr[0][4][0]
        except:
            print('Failed domain!')

    def get_dir(self):
        address = 'http://' + str(self.domain)
        d = Dir_Scanner(address)
        d.more_threads()

    def get_port(self):
        n = NmPortScanner(self.ipaddress)
        n.scan()
        n.print_result()


if __name__ == '__main__':
    m = main()