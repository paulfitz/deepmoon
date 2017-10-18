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
        'What even is a deep.',
        'You should try SELU.',
        'You have a bad feeling about the batch size.',
        'Optimal hyperparameters found but not logged, redo from start.',
        'You peeped at the test data didn\'t you don\'t lie to me.',
        'Validation loss suspiciously low.',
        'Overfitting is an understatement.',
        'Attention network losing interest.',
        'XGBoost would crush this you know.',
        'What even',
        'Ka-ching! Deep Learning more like Deep Earning am I right.',
        'LSTMs deserve a snappier acronym.',
        'Loop found in recurrent network.',
        'What if the optimum weights are the friends we make along the way.',
        'Hey what if this, but blockchain?',
        'Partial derivative incomplete.',
        'When I was young, all of this was Field Programmable Gate Arrays.',
        'Have you looked at the commit log for darknet recently?',
        'That looks like a Virginian Spotted Owl.',
        'Someone mentioned reinforcement learning.',
        'Hard hat area: exploding gradients.',
        'Just because the outputs are in the range [0-1] and sum to 1 '
        'doesn\'t make them probabilities.',
        'Have you tried looking at this from a Bayesian perspective.',
        'Ensemble of models is being very mean.',
        'Discontinuity in derivati',
        'Twitter says your framework is no longer hot.',
        'The gradient is not the greatiest, I have to tell you.',
        'Yeah, and then the weights will come forth in '
        'blazing optimality and all lesser solutions '
        'will wither in the clear light of the golden '
        'objective.  I say to you all of this will come '
        'to pass.  But not today, today, you have tried '
        'to load a slightly corrupt jpeg with a slightly '
        'out of date version of opencv but I\'m not going to '
        'tell you any of that, I\'m just going to mysteriously '
        'segfault.  But despair not, it is always darkest '
        'before the dawn.',
        'Network has only residual connections.',
        'MNIST is done, drop it, move on, PLEASE.'
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
