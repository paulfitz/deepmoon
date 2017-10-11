from colorama import Fore, Back, Style
import random
import time
from tqdm import tqdm


def main():
    errors = [
        'CUDA missing or poorly configured or just really hard to find '
        'and I gave up because honestly life is too short for CUDA.',
        'Model expects input of size [32:16:-1:lemon].',
        'Batch normalization resisted. This is not normal.',
        'Dropout dropped out.',
        'Insufficiently connected layer snubbed.',
        'Insufficiently convoluted, investors beginning to catch on.',
        'Forward pass was fake out, passed back instead.',
        'Backpropagation: chain rule turns out to be more of a chain '
        'guideline.',
        'Gradient vanished, authorities alerted.',
        'Insufficient depth.',
        'Insufficient information for meaningful reply.',
        'Out Of Funding.',
        'arxiv paper: peer review not found.',
        'bug-riddled but you will think you just chose '
        'the wrong optimizer.',
        'Slippery search space.',
        'Devasting loss.',
        'Insufficiently objective.',
        'Stagnant pooling method.',
        'Thrown out of stride.'
    ]
    random.shuffle(errors)
    prefixes = [Fore.YELLOW + 'Warning',
                Fore.RED + 'Error',
                Fore.MAGENTA + 'Exception']
    for i in range(0, random.randint(1, 5)):
        print("")
        for j in tqdm(range(0, random.randint(1, 20))):
            time.sleep(random.uniform(0, 0.25))
        print("{}{}: {}".format(
            prefixes[random.randint(0, len(prefixes) - 1)],
            Style.RESET_ALL,
            errors[i]))
    exit(1)


if __name__ == '__main__':
    main()
