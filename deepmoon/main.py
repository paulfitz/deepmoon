import argparse
from colorama import Fore, Style
from deepmoon.errors import Errors
from deepmoon.missing_from_tensorflow import list_missing_things
import random
import time
from tqdm import tqdm


def main():
    parser = argparse.ArgumentParser(description="the deep learning framework "
                                     "from beyond the moon")
    parser.add_argument('--darknet', action='store_true',
                        help='read from darknet commit logs')
    parser.add_argument('--brooklyn', action='store_true',
                        help='use hand-crafted artisanal error messages')
    parser.add_argument('--cuda', action='store_true',
                        help='omg don\'t talk to me about cuda')
    parser.add_argument('--missing', action='store_true',
                        help='list some missing things')
    parser.add_argument('--sweat', type=int,
                        help='run an easy training run (with sweat=0) or '
                        'a hard one (sweat=5).  If your model hasn\'t been '
                        'converging, why not relax with a no-sweat training '
                        'run just for a change of pace?')

    args = parser.parse_args()

    flavor = 'artisanal'
    errors = ['bloody CUDA']  # safe default
    if args.missing:
        list_missing_things()
        return
    if args.sweat is not None:
        sweat = int(args.sweat)
        from deepmoon.potemkin import show_training_run
        show_training_run(sweat=sweat)
        return
    if args.darknet:
        flavor = 'darknet'
    elif args.brooklyn:
        flavor = 'artisanal'
    elif args.cuda:
        flavor = 'cuda'
    errors = Errors(filename='.deepmoon', flavor=flavor)
    prefixes = [Fore.YELLOW + 'Warning',
                Fore.RED + 'Error',
                Fore.MAGENTA + 'Exception']
    for i in range(0, random.randint(1, 5)):
        for j in tqdm(range(0, random.randint(1, 20))):
            time.sleep(random.uniform(0, 0.25))
        error = errors.get()
        print("{}{}: {}".format(
            prefixes[random.randint(0, len(prefixes) - 1)],
            Style.RESET_ALL,
            error))
    exit(1)


if __name__ == '__main__':
    main()
