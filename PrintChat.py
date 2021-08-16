class PrintChat:
    def __init__(self, text, user):
        self.__cutpoint = 50
        self.text = ''
        self.user = ''

    def print_message(self):
        len_text = len(self.text)
        start_str = ''
        end_str = ''

        if len_text < self.cutpoint:
            for char in range(len_text):
                start_str += '_'
                end_str += '-'

            text_str = '(' + text + ')'
            print(' ' + start_str)
            print(text_str)
            print(' ' + end_str)

        else:
            for char in range(self.cutpoint):
                start_str += '_'
                end_str += '-'
            split_strings = []
            for index in range(0, len_text, cutpoint):
                split_strings.append(text[index: index + cutpoint])
            print(' ' + start_str)
            print('/' + split_strings[0] + '\\')
            split_strings.pop(0)
            last_element = split_strings.pop()
            for string in split_strings:
                print('|' + string + '|')
            last_element_len = len(last_element)
            if last_element_len < cutpoint:
                to_sum = cutpoint - last_element_len
                for space in range(to_sum):
                    last_element += ' '
            print('\\' + last_element + '/')
            print(' ' + end_str)
