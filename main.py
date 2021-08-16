import os

from Ansi import Ansi
from PrintChat import PrintChat
from Interface import Interface

try:
    import amino
except ModuleNotFoundError:
    os.system('pip3 install amino.py==1.2.17')
    import amino

#creds = Interface.get_creds(None)
creds = {
    'email': 'email',
    'password': 'contraseña',
}
client = amino.Client()

client.login(**creds)
comid = Interface.get_comId(None)
subclient = amino.SubClient(comId=comid, profile=client.profile)
client.session.close()
subclient.session.close()

class Main():
    def __init__(self):
        pass

    def main(self):
        @client.event('on_text_message')
        def on_text_message(data):
            print(f'{data.message.authot.nickname}: {data.message.content}')
            #new_text_object = PrintChat({data.message.content}, {data.message.author.nickname})

        @client.event('on_group_member_join')
        def on_group_member_join(data):
            Interface.cprint(f'bienvenid@, <$@{data.message.author.nickname}$>.', 'green')

if __name__ == '__main__':
    Main.main(None)
