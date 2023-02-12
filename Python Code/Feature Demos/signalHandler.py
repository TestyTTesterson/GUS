import sys
import time
import signal
from functools import partial

def interrupt_handler(signum, frame, ask=True):
    print(f' Handling signal {signum} ({signal.Signals(signum).name}).')
    if ask:
        signal.signal(signal.SIGINT, partial(interrupt_handler, ask=False))
        print('To confirm interrupt, press ctrl-c again.')
        return

    print('Cleaning/exiting...')
    # do whatever...
    time.sleep(1)
    sys.exit(0)
    # do whatever...
    print('testing inside handler def')
    time.sleep(0.3)



def main():
    while True:
        print('.', end='', flush=True)
        time.sleep(0.3)


if __name__ == '__main__':
    print('testing inside _name_ def, before signal')

    signal.signal(signal.SIGINT, interrupt_handler)
    print('testing inside _name_ def, after signal')

    main()