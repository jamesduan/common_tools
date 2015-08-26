
import paramiko

class SFtpManager(object):
    ''' sftp manager for linux or unix.'''
    def __init__(self, host='', port=22, username='', password=''):
        args = (host, port)
        self.t = paramiko.Transport(args)
        self.t.connect(username=username, password=password)
        self.sftp_client = paramiko.SFTPClient.from_transport(t)

    def put(self, local_path='', remote_path='', callback=None):
        try:
            self.sftp_client.put(local_path, remote_path, callback=callback)
            print "upload over."
        except Exception , e:
            print str(e)

    def get(self, remote_path='', local_path='', callback=None):
        try:
            self.sftp_client.get(remote_path, local_path)
        except Exception, e:
            print str(e)

    def __del__(self):
        self.t.close()
