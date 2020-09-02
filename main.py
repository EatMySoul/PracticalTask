from pynput import keyboard
import time
import tkinter as Tk
from code import CODE
import os




class Programm():

    def __init__(self):
        with open('practicalTasks.txt','r') as text:
            selector_data = text.read().split('\n')[:-1]
        with open('practicalTasks.txt','r') as text:
            kostil_selector_data = text.read().split('\n')[:-1]   # Почему так $#&#! ?
        self.code = CODE
        self.selector = Selector(selector_data)

        while True:
            self.choose = self.selector.job()
            print(kostil_selector_data[self.choose])
            self.execute_code(self.choose)
            input()
            #block_scheme = Block_Scheme(self.code[self.choose]) unworked
            #input()

    def job(): #am i need it?
        pass
    
    def execute_code(self,selector_choose):
        exec(self.code[selector_choose])

    def get_code(self,selector_choose):
        return self.code[selector_choose]



class Selector():

    def __init__(self,selector_data):
        self.selector_data = selector_data
        self.data_count = len(self.selector_data) - 1
        #cuting 

        for i in range(self.data_count):
            self.selector_data[i] = self.selector_data[i][:120] + (self.selector_data[i][120:] and "...")
            print('dowork')

        self.selector_position = 0
        self.terminal_columns = int(os.popen('stty size','r').read().split()[0]) - 1
        self.border_above = 0
        self.border_below = self.terminal_columns - 1  


    def job(self): 
        os.system('clear')
        self.selector_show()
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
        input()
        return self.selector_position

    def on_press(self,key):
        os.system('clear')

        if key == keyboard.Key.up:
            if self.selector_position == 0:
                self.border_below = self.data_count + 1
                self.border_above = self.data_count - self.terminal_columns + 1 
                self.selector_position = self.data_count
            else:
                if self.selector_position == self.border_above:
                    self.border_below -= 1
                    self.border_above -= 1
                self.selector_position -= 1
                
        elif key == keyboard.Key.down:
            if self.selector_position == self.data_count:
                self.border_below = self.terminal_columns - 1
                self.border_above = 0
                self.selector_position = 0
            else:
                if self.selector_position == self.border_below - 1:
                    self.border_below += 1
                    self.border_above += 1
                self.selector_position += 1

        elif key == keyboard.Key.enter:
            return False
        
        elif key == keyboard.Key.esc:
            exit(0)

        os.system('clear')
        self.selector_show()

    def selector_show(self):
        start = self.border_above if self.border_above > 0 else 0
        end = self.border_below if self.border_below < self.data_count else self.data_count + 1

        for i in range(start,end):
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
            elif True:                                  #not true
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
                

    def show_scheme(self,text):                         #todo
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

