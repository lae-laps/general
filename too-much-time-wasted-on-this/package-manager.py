import os
import requests

class Ansi:
    def __init__(self) -> None:
        self.__color_dict = {
            'green': '82',
            'dark-green': '149',
            'red': '196',
            'orange': '208',
            'white': '15'
        }

    def cprint(self, content, color) -> int:
        if content.endswith('/notnewline'):
            print('\033[38;5;' + self.__color_dict[color] + 'm' + content + '\033[m', end='')
        else:
            print('\033[38;5;' + self.__color_dict[color] + 'm' + content + '\033[m')
        return 0

    def cinput(self, prompt, color):
        print('\033[' + self.__color_dict[color] + '', end='')
        output = input()
        return output

    def cmenu(self, options) -> int:
        # Returns int corresponding to option 
        for option in range(len(options)):
            self.cprint('[/notnewline', 'green')
            num_str = option + '/notnewline'
            self.cprint(num_str, 'orange')
            self.cprint(None, '] ~ /notnewline', 'green')
            self.cprint(None, options[option+1], 'green')
        while True:
            output = int(self.cinput('>> ', 'orange'))
            if output > 0 and output < len(options):
                return output
            else:
                self.cprint('Invalid option ~> Enter a valid number between 0 and ' + len(options), 'orange')
                continue

class CheckData():
    def __init__(self) -> None:
        pass

    def chech_url_exist(self, url) -> bool:
        response_code = requests.get(url)
        response_start = ''
        for char in range(response_code):
            if char < 12:
                response_start += response_code[char]
            else:
                break
        if response_start == '<Response [2':
            return True
        else:
            return False

    def check_repo_exits(self, url) -> bool:
        is_https = ''
        for char in range(url):
            if char < 9:
                is_https += url[char]
            else:
                break
        if is_https != 'https://':
            url += 'https://'
        exists = self.chech_url_exist(url)
        if exists == True:
            return True
        else:
            return False

class Upload:
    def __init__(self) -> None:
        self.upload_path = ''
        self.origin = ''
        self.commit_name = ''
        self.create_repo = None
        self.olibs_user = None

    def set_upload_conditions(self) -> int:
        # Setup data
        while True:
            repo_exists = Ansi.cmenu(None, ['Upload to existing repository', 'Create new repository'])
            if repo_exists == 1:
                self.create_repo = False
                upload_user = Ansi.cmenu(['Upload to OpenLibs Github', 'Upload to your Github ~ Requires your token'])
                if upload_user == 1:
                    self.olibs_user = True
                    while True:
                        repo_name = Ansi.cinput('Repository name: ', 'green')
                        repo_name = 'https://github.com/OpenLibs-Project/' + repo_name
                        is_valid = CheckData.check_repo_exists(repo_name)
                        if is_valid == True:
                            self.origin = repo_name
                            while True:
                                commit_name = Ansi.cinput('Commit name: ', 'green')
                                for char in commit_name():
                                    if char == ' ':
                                        valid_commit_name = False
                                        break
                                    else:
                                        valid_commit_name = True
                                if valid_commit_name == True:
                                    self.commit_name = commit_name
                                else:
                                    Ansi.cprint('Invalid comit name ~ Cannot include spaces')
                        else:
                            Ansi.cprint('Invalid repository name ~ Doesnt exist ~ Create one or enter valid name', 'red')
                            Ansi.cprint('View valid repositories at https://github.com/OpenLibs-Project/', 'green')
                else:
                    self.olibs_user = False
                    while True:
                        repo_url = Ansi.cinput('Enter full repository URL: ', 'green')
                        is_valid_url = CheckData.check_repo_exits()
                        if is_valid_url == True:
                            self.origin = repo_url
                            while True:
                                commit_name = Ansi.cinput('Commit name: ', 'green')
                                for char in commit_name():
                                    if char == ' ':
                                        valid_commit_name = False
                                        break
                                    else:
                                        valid_commit_name = True
                                if valid_commit_name == True:
                                    self.commit_name = commit_name
                                else:
                                    Ansi.cprint('Invalid comit name ~ Cannot include spaces')
                        else:
                            Ansi.cprint('Invalid URL ~ Try again', 'red')
            else:
                self.create_repo = True
        return 0

    def upload(self) -> int:
        os.system('cd ' + self.upload_path)
        os.system('git remote add origin ' + self.origin)
        dir_files = os.system('ls')
        for file in dir_files:
            os.system('git add ' + file)
        os.system('git commit -m ' + self.commit_name) 
        print('')
        os.system('git push origin master')
        return 0

class Download:
    def __init__(self) -> None:
        self.clone_url = ''
        self.is_entire_repo = None

    def set_download_conditions(self):
        while True:
            clone_url = Ansi.cinput(None, 'Clone URL: ', 'green')
            exists = CheckData.check_repo_exits(clone_url)
            if exists == True:
                continue
            else:
                Ansi.cprint('Invalid URL ~ Does not exist', 'red')

if __name__ == '__main__':
    Download.set_download_conditions(None)
