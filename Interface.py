import amino
from Ansi import Ansi

class Interface:
    def __init__(self):
        self.client = amino.Client()

    def create_menu(self):
        pass

    def get_creds(self):
        email = input(Ansi.cprint('Introduzca el email: ', 'green'))
        password = input(Ansi.cprint('Introduzca la contraseña: ', 'green'))
        want_to_save = input(Ansi.cprint('Quieres guardar tu login ~ [y/N]: ')).lower()
        if want_to_save == 'y':
            pass
        creds = {
            'email': email,
            'password': password
        }
        return creds

    def get_comId(self):
        options = ['Login with aminoId', 'Login with comId']
        result = Ansi.cmenu(options)
        if result == 1:
            aminoid = Ansi.cinput('AminoId: ')
            return self.client.search_community(aminoid).comId[0]
        else:
            comid = Ansi.cinput('ComId: ')
            return comid

    def banner(self):
        pass

    def clear():
        pass
    