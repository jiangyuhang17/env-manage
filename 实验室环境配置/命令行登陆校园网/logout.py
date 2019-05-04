import urllib2
import urllib

class Loginer():
    def __init__(self, username, password):
        self.loginUrl = 'https://login.ecnu.edu.cn/srun_portal_pc.php?ac_id=1&'
        self.username = username
        self.password = password
        self.openner = urllib2.build_opener()

    def login(self):
        postdata = {
            'username': self.username,
            'info': '',
            'action': 'auto_logout',
            'usr_ip': '219.228.135.110'
        }
        postdata = urllib.urlencode(postdata)
        myRequest = urllib2.Request(url=self.loginUrl, data=postdata)

        if(str(self.openner.open(myRequest).read()).find('font-weight:bold;color:orange')!=-1):
            print 'logout successfully'

def main():
    file=open('username.log','r')
    username=file.readline()
    print username
    l = Loginer(username,'')
    l.login()

if __name__ == '__main__':
    main()
    print 'done'