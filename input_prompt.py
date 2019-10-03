import readline

def rlinput(prompt, prefill=''):
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)
    finally:
        readline.set_startup_hook()

if __name__ == '__main__':
    print("Original input()")
    out = input("Prompt>> ")
    print("out is {}".format(out))

    print("rlinput(prefill Steven)")
    out = rlinput("Prompt>> ", "Steven")
    print("out is {}".format(out))
