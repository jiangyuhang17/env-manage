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
            'password': self.password,
            'action': 'login',
            'ac_id': '1',
            'user_ip':'',
            'nas_ip':'',
            'user_mac':'',
            'url':''
        }
        postdata = urllib.urlencode(postdata)
        myRequest = urllib2.Request(url=self.loginUrl, data=postdata)

        result = self.openner.open(myRequest).read()
        resStr=str(result)
        if(resStr[1] == 'h'):
            print 'connected successfully'
        else:
            print 'connected faild!! Maybe your username or password is wrong!'

def main():
    username=raw_input('Enter your username:')
    password=raw_input('Enter your password:')
    file=open('username.log','w')
    file.write(username)
    file.close()
    l = Loginer(username,password)
    l.login()

if __name__ == '__main__':
    main()
    print 'done'