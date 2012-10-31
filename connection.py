import re, pexpect

class ConnectionException(Exception):
    pass

class Connection():
    """
    A telnet connection to a Technicolor Gateway router.
    This class will let you execute telnet commands programmatically and get
    their output.
    """
    def __init__(self, ip, username, password, method="telnet", connect=True):
        """
        initialise a connection.
        Args:
          ip (str): IP address of the device
          username (str): username to use when logging in
          password (str): the password for that username
          method (str): "telnet" is the only currently supported option (default)
          connect (boolean): True to connect straight away (default)
        """
        self.conn = None
        self.ip = ip
        self.username = username
        self.password = password
        self.method=method
        self.prompt = r'({' + self.username + '})(([A-Za-z0-9\[\]]+)?)=>'

        if (connect):
            self.connect()
        
    def connect(self):
        """
        Connect to and log into the router.
        """
        if (self.conn):
            raise ConnectionException("Already connected")
        assert(self.method == "telnet")  # others aren't supported yet.
        
        self.conn = pexpect.spawn('telnet ' + self.ip)
        #handle login.
        self.conn.expect('Username :')
        self.conn.sendline(self.username + "\r")
        self.conn.expect('Password :')
        self.conn.sendline(self.password + "\r")
        self.conn.expect(self.prompt)

    def run(self, cmd):
        """
        Run a command.
        """
        #remove trailing newlines
        while (cmd[-1:] == '\r' or cmd[-1:] == '\n'):
            cmd = cmd[:-1]

        self.conn.sendline(cmd + '\r')
        self.conn.expect(self.prompt)
        return self.conn.before

    def disconnect(self):
        """
        Disconnect and shut down telnet session.
        """
        self.run('exit')
        self.conn.close()
    
