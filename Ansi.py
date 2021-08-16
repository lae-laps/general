class Ansi():
    def __init__(self):
        self.color_dict = {
            "red": "196",
            "green": "149",
            "orange": "208"
        }

    def clear(self):
        print('\033[2J')

    def cprint(self, content, color):
        color_code = self.color_dict[color] + "m"
        to_print_start = "\033[38;5;"
        to_print_end = "\033[m"
        to_print = to_print_start + color_code + content + to_print_end
        print(to_print)

    def cinput(self, prompt, color):
        color_code = self.color_dict[color] + "m"
        to_prompt_start = "\033[38;5;"
        to_prompt_end = "\033[m"
        to_prompt = to_prompt_start + color_code + prompt + to_prompt_end
        result = input(to_prompt)
        return result

    def cmenu(self, options):
        for option in range(len(options)):
            self.cprint('[' + option + '] ~ ' + options[option], 'green')
        while True:
            result = int(self.cinput('>> '))
            if result > 0 and result < len(options) + 1:
                return result
            else:
                self.cprint('Input no válido', 'red')
                