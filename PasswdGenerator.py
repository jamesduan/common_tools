# encoding:utf8 

import string, random

class PasswdGenerator(object):

    ''' '''

    def __init__(self, length = None):

        self.passwd_length = length
        self.lowercase = list(string.lowercase)
        self.uppercase = list(string.uppercase)
        self.digits = list(string.digits)

    def generate(self):

        tmp_pass = []
        pass_str = ""

        if self.passwd_length == None:

            return None

        else :

            while(True):

                lower_pass = random.sample(self.lowercase, 1)
                upper_pass = random.sample(self.uppercase, 1)
                digit_pass = random.sample(self.digits, 1)
                pass_str = pass_str + lower_pass[0] + upper_pass[0] + digit_pass[0]
                tmp_pass.append(pass_str)

                if len(tmp_pass) > self.passwd_length:
                    password = ""
                    for item in random.sample(tmp_pass, len(tmp_pass)):
                        password += item

                    return password[:self.passwd_length]

if __name__ == "__main__":
    ge = PasswdGenerator(8)
    print ge.generate()

