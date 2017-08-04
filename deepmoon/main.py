import random
import time


def main():
    errors = [
        'CUDA missing or poorly configured or configured but ignored '
        'or not needed',
        'Library name missing',
        'Dependency fault in library configuration logging aggregator',
        'Model expects input of size lemon:16:-1:lemon',
        'Problem: insufficiently deep',
        'Batch insufficiently normalized',
        'Dropout dropped out',
        'Insufficiently connected layer',
        'Insufficiently convoluted',
        'Forward pass was fake out',
        'Backpropagation: exception found in chain rule',
        'Gradient vanished'
    ]
    random.shuffle(errors)
    for i in range(0, random.randint(1, 5)):
        time.sleep(1)
        print(errors[i])
    exit(1)


if __name__ == '__main__':
    main()
