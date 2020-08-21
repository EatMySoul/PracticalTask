from pynput import keyboard
import os
"""
todo:
    1) selector
    2) block-schmeme of task
    3) task
"""



class Programm():

    def __init__(self):
        self.selector = Selector()
        self.choose = self.selector.job()
        self.code = ["""print('a')
if 1 > 2:
    print('noo')
else:
    print('heheh')
"""]
        block_scheme = Block_Scheme(self.code[self.choose])

    def job(): #am i need it?
        pass
    
    def execute_code(self,selector_choose):
        exec(self.code[selector_choose])

    def get_code(self,selector_choose):
        return self.code[selector_choose]


class Selector():

    def __init__(self):
        self.selector_data = ('1. Вычислить сумму элементов числового массива A = (a1 , a2 , ... , aN ).','2',3,4,5)
        self.data_count = len(self.selector_data) - 1
        self.selector_position = 0
        self.selector_show()

    def job(self): 
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
        input()
        return self.selector_position

    def on_press(self,key):
        os.system('clear')
        if key == keyboard.Key.up:
            if self.selector_position == 0:
                self.selector_position = self.data_count
            else:
                self.selector_position -= 1
        elif key == keyboard.Key.down:
            if self.selector_position == self.data_count:
                self.selector_position = 0
            else:
                self.selector_position += 1
        elif key == keyboard.Key.enter:
            return False
        os.system('clear')
        self.selector_show()

    def selector_show(self):
        for i in range(self.data_count + 1):
            if i == self.selector_position:
                print('\033[42m',self.selector_data[i],'\033[0m',sep='')
            else:
                print(self.selector_data[i])

class Block_Scheme():

    def __init__(self,code_text):
        self.code_text = code_text.split('\n')
        self.block_scheme = self.get_scheme_struct()
        print(self.block_scheme)
        self.show_scheme(self.block_scheme)

    def get_scheme_struct(self):
        self.step = 0
        block_scheme = []
        block_scheme = self.code_parser(block_scheme)
        return block_scheme

    def code_parser(self,block_scheme,tab = 0):
        while self.code_text[self.step][:tab] == tab*' ' and self.step < len(self.code_text) -1:
            string = self.code_text[self.step]
            if 'print' in string or 'input' in string:
                block_scheme.append(string)
                self.step += 1
            elif True:
                temp_scheme = [string]
                tab += 4
                self.step += 1
                temp_scheme = self.code_parser(temp_scheme,tab)
                tab -= 4
                if 'if' in string:
                    block_scheme.append([temp_scheme])
                elif 'else' in string:
                    block_scheme[-1].append(temp_scheme)
                elif 'for' in string:
                    block_scheme.append(temp_scheme)
        print('deep work')
        return block_scheme
                

    def show_scheme(self,text):
        for string in text:
            if type(string) == list:
                self.show_scheme(string)
            else:
                print(string)



def main():
    os.system('clear')
    proc1 = Programm()

if __name__ == "__main__":
    main()

