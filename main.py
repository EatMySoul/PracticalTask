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
        self.choose = self.selector.start()
        print(self.choose)

class Selector():

    def __init__(self):
        self.selector_data = (1,2,3,4,5)
        self.choose_count = len(self.selector_data) - 1
        self.selector_position = 0
        self.selector_show()

    def start(self): 
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
        input()
        return self.selector_position

    def on_press(self,key):
        os.system('clear')
        if key == keyboard.Key.up:
            if self.selector_position == 0:
                self.selector_position = self.choose_count
            else:
                self.selector_position -= 1
        elif key == keyboard.Key.down:
            if self.selector_position == self.choose_count:
                self.selector_position = 0
            else:
                self.selector_position += 1
        elif key == keyboard.Key.enter:
            return False
        self.selector_show()

    def selector_show(self):
        for i in range(self.choose_count + 1):
            if i == self.selector_position:
                print('\033[42m',self.selector_data[i],'\033[0m',sep='')
            else:
                print(self.selector_data[i])


class Block_Scheme():

    def __init__(self):
        pass

    def finder():
        pass

    def adder(t):
        pass

def main():
    proc1 = Programm()

if __name__ == "__main__":
    main()
