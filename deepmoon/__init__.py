from deepmoon.errors import Errors


ERRORS = {
    'all': None,
    'key': ''
}


def configure(filename=None, flavor=None):
    key = "{} {}".format(filename, flavor)
    if key != ERRORS['key']:
        unconfigure()
    if ERRORS['all'] is None:
        ERRORS['all'] = Errors(filename=filename,
                               flavor=flavor)
        ERRORS['key'] = key
    return ERRORS['all']


def configure_if_needed():
    if ERRORS['all'] is None:
        configure()
    return ERRORS['all']


def unconfigure():
    ERRORS['all'] = None
    ERRORS['key'] = ''


def error():
    '''
    Returns: a deep error.
    '''
    return configure_if_needed().get()
