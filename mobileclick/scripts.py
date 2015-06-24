# -*- coding:utf-8 -*-

MOBILECLICK_URL = 'http://www.mobileclick.org'
DOCUMENT_A_TEXT = 'Document Collection (~ 1GB)'
SUBSET_A_TEXT = 'Subset (~ 50MB)'

def main(istest=False):
    import sys, os, getpass
    email = os.environ.get('MOBILECLICK_EMAIL', None)
    password = os.environ.get('MOBILECLICK_PASSWORD', None)
    if email is None or password is None:
        # if env variables are not set
        print "Please input the email and password for %s" % MOBILECLICK_URL
        sys.stdout.write('Email: ')
        email = raw_input()
        password = getpass.getpass()
    if login(email, password):
        links = find_download_links(istest)
        for link in links:
            filename = download_file(link)
            deploy_data(filename)
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
    return filename

def find_download_links(istest):
    import urllib2, BeautifulSoup
    res = urllib2.urlopen('%s/home/data' % MOBILECLICK_URL)
    html = BeautifulSoup.BeautifulSoup(res.read())
    def is_download_link(node):
        return node.name == 'a' and node.getText() == 'Download'
    link = html.find(is_download_link)['href'] + '?dl=1'
    atext = SUBSET_A_TEXT if istest else DOCUMENT_A_TEXT
    def is_download_doclink(node):
        return node.name == 'a' and node.getText() == atext
    doclink = html.find(is_download_doclink)['href'] + '?dl=1'
    return (link, doclink)

def deploy_data(filename):
    import os, tarfile, zipfile, glob
    if tarfile.is_tarfile(filename):
        with tarfile.open(filename, 'r') as tf:
            tf.extractall('./data')
    for filepath in glob.glob('./data/*/*.zip'):
        basedir = os.path.dirname(filepath)
        if zipfile.is_zipfile(filepath):
            with zipfile.ZipFile(filepath, 'r') as zf:
                zf.extractall(basedir + '/')

if __name__ == '__main__':
    main()
