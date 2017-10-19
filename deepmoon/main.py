import argparse
from colorama import Fore, Style
import dataset
import importlib
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
    args = parser.parse_args()

    flavor = 'artisanal'
    errors = ['bloody CUDA']  # safe default
    if args.darknet:
        flavor = 'darknet'
    elif args.brooklyn:
        flavor = 'artisanal'
    source = importlib.import_module('deepmoon.{}'.format(flavor))
    errors = source.fetch_messages()
    db = dataset.connect('sqlite:///.deepmoon')
    seen = db[flavor]
    seen.create_column_by_example('comment', 'Snarky remark')
    seen.create_index('comment')
    random.shuffle(errors)
    prefixes = [Fore.YELLOW + 'Warning',
                Fore.RED + 'Error',
                Fore.MAGENTA + 'Exception']
    at = 0
    tqdm.get_lock().locks = []  # work around a new android issue
    for i in range(0, random.randint(1, 5)):
        for j in tqdm(range(0, random.randint(1, 20))):
            time.sleep(random.uniform(0, 0.25))
        while seen.count(comment=errors[at]) > 0:
            at += 1
            if at == len(errors):
                at = 0
                seen.delete()
        print("{}{}: {}".format(
            prefixes[random.randint(0, len(prefixes) - 1)],
            Style.RESET_ALL,
            errors[at]))
        seen.insert({'comment': errors[at]})
    exit(1)


if __name__ == '__main__':
    main()
