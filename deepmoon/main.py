from colorama import Fore, Style
import dataset
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
        'Thrown out of stride.',
        'Insufficient activation, call number on card to activate.',
        'Softmax more like Hardmin right now.',
        'Sigmoid is a great name for a dog.',
        'What even is a deep.'
    ]
    db = dataset.connect('sqlite:///.deepmoon')
    seen = db['seen']
    seen.create_column_by_example('comment', 'Snarky remark')
    seen.create_index('comment')
    random.shuffle(errors)
    prefixes = [Fore.YELLOW + 'Warning',
                Fore.RED + 'Error',
                Fore.MAGENTA + 'Exception']
    at = 0
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
