# -*- coding:utf-8 -*-

MOBILECLICK_URL = 'http://www.mobileclick.org'

def download_mobileclick_data():
    import sys, getpass
    print "Please input the email and password for %s" % MOBILECLICK_URL
    sys.stdout.write('Email: ')
    email = raw_input()
    password = getpass.getpass()
    if login(email, password):
        links = find_download_links()
        for link in links:
            download_file(link)
    else:
        print "Login failed"

def login(email, password):
    import urllib, urllib2, BeautifulSoup, re
    # cookie setting
    cookie = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(cookie)
    urllib2.install_opener(opener)

    # get the token
    res = urllib2.urlopen('%s/users/sign_in' % MOBILECLICK_URL)
    html = BeautifulSoup.BeautifulSoup(res.read())
    loginform = html.find('form', {'id': 'new_user'})
    token = loginform.find('input', {'name': 'authenticity_token'})['value']

    # login
    values = {'user[email]': email, 'user[password]': password}
    data = urllib.urlencode(values)
    req = urllib2.Request('%s/users/sign_in' % MOBILECLICK_URL, 
        data, {'X-CSRF-Token': token, 'Referer': '%s/users/sign_in' % MOBILECLICK_URL})
    res = urllib2.urlopen(req)
    result = BeautifulSoup.BeautifulSoup(res.read())
    suc = result.find('div', {'class': re.compile(r'\balert-success\b')})

    # login success?
    return True if suc else False

def download_file(url):
    import sys, urllib2
    filename = url.split('/')[-1]
    filename = filename.split('?')[0]
    res = urllib2.urlopen(url)
    meta = res.info()
    filesize = int(meta.getheaders("Content-Length")[0])
    print "Downloading: {0} Bytes: {1}".format(url, filesize)

    filesize_obtained = 0
    blocksize = 8192
    with open(filename, 'wb') as f:
        while True:
            buf = res.read(blocksize)
            if not buf:
                break
            filesize_obtained += len(buf)
            f.write(buf)
            p = float(filesize_obtained) / filesize
            status = r"{0}  [{1:.2%}]".format(filesize_obtained, p)
            status += "[%s]" % ('*'*int(p*100) + ' '*(100 - int(p*100)) )
            status += chr(8)*(len(status)+1)
            sys.stdout.write(status)
            sys.stdout.flush()
    print
    print "Downloaded: {0}".format(url)

def find_download_links():
    import urllib2, BeautifulSoup
    res = urllib2.urlopen('%s/home/data' % MOBILECLICK_URL)
    html = BeautifulSoup.BeautifulSoup(res.read())
    def is_download_link(node):
        return node.name == 'a' and node.getText() == 'Download'
    link = html.find(is_download_link)['href'] + '?dl=1'
    def is_download_doclink(node):
        return node.name == 'a' and node.getText() == 'Document Collection (~ 1GB)'
    doclink = html.find(is_download_doclink)['href'] + '?dl=1'
    return (link, doclink)

if __name__ == '__main__':
    download_mobileclick_data()
