import argparse
parser = argparse.ArgumentParser(description="information collecting tool")

parser.add_argument('-d', '--dir', action='store_true', help="Burp force directory")
parser.add_argument('-p', '--port', action='store_true', help="Port scan")
parser.add_argument('-w', '--whois', action='store_true', help="Get whois information")
parser.add_argument('-c', '--cms', action='store_true', help="Get CMS type")
parser.add_argument('-s', '--sub', action='store_true', help="Search subdomain")
parser.add_argument('-t', '--test', action='append')
parser.add_argument('url')

args = parser.parse_args()

if args.dir:
    print("dir is OK!")
if args.port :
    print("port is OK!")
if args.whois :
    print("whois is OK!")
if args.cms :
    print("cms is OK!")
if args.sub :
    print("sub is OK!")
if args.url:
    print(args.url)

if args.test:
    print(args.test)