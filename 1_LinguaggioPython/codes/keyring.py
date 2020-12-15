import hashlib


class keyring:
    def __init__(self):
        '''
        Le coppie (password, chiave) sono memorizzate in un dizionario
        '''
        self.passwords = {}

    def __get__(self, inst, cls):
        '''
        Per l'accesso viene richiesta la password, il cui valore hash deve
        coincidere con il valore hash memorizzato
        '''
        try:
            k, v = self.passwords[inst]
        except KeyError:
            print(f"Unknown user {inst.user}")
            return None
        passwd = input("Enter password: ")
        h = hashlib.sha256(bytes(passwd, 'utf-8')).hexdigest()
        if k == h:
            return v
        print("Wrong password")
        return None
        
    def reset(self, inst, key):
        '''
        Inserisce una nuova chiave e resetta la password
        '''
        passwd = input("Enter new password: ")
        h1 = hashlib.sha256(bytes(passwd, 'utf-8')).hexdigest()
        passwd = input("Repeat password: ")
        h2 = hashlib.sha256(bytes(passwd, 'utf-8')).hexdigest()
        if h1 != h2:
            print('Passwords differ!')
        else:
            self.passwords[inst] = (h1, key)
            print("Password correctly set!")
            
    def __set__(self, inst, key):
        '''
        Chiamata ogni volta che si cerca di inserire un nuovo valore della chiave
        '''
        try:
            k, v = self.passwords[inst]
        except KeyError:
            self.reset(inst,key)
        else:
            passwd = input("Enter password: ")
            h = hashlib.sha256(bytes(passwd, 'utf-8')).hexdigest()
            if h == k:
                self.reset(inst, key)
            else:
                print('Wrong password!')


class user:
    def __init__(self, name):
        self.user = name
    key = keyring()


if __name__ == "__main__":
    u1 = user("Luca")
    u1.key = "my secret key!"
    print(u1.key)
    print(u1.key.passwords)