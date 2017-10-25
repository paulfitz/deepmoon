
import cowsay
import datetime
import time


def list_missing_things():

    acts = [
        ('use SSE4.2 instructions', 'could speed up CPU computations'),
        ('use AVX instructions', 'could speed up CPU computations'),
        ('use AVX2 instructions', 'could speed up CPU computations'),
        ('use FMA instructions', 'could speed up CPU computations'),
        ('share PIECES of cheese', 'could fill up a CASE of the nibbles'),
        ('offer THOUGHTS on your love life',
         'could be more INTERESTING than cheese'),
        ('like TWEETS about memes', 'could kill some TIME between epochs'),
        ('tickle YOU with its tentacles',
         'so MIGHT AS WELL USE THEM TICKLE TICKLE'),
        ('have FEELINGS', 'might greatly COMPLICATE our relationship'),
        ('make friends with BUGS',
         'could be more FUN than training your model'),
        ('use RESISTORS against the status quo',
         'so VIVE LA REVOLUTION'),
        ('flash PIXELS in steganographic patterns',
         'so blink BLINK blinkety-blink'),
        ('collide miniature BLACK HOLES together',
         'could speed up GRAVITATIONAL collapse'),
        ('count the number of BIRDS in the heavens',
         'they are NOT going to count themselves'),
        ('test your patience with DELAYS',
         'have you noticed that they seem be be getting LONGER '
         'exponentially')
    ]

    tick = 0.04
    for avail, outcome in acts:
        now = datetime.datetime.now()
        print("{}: W tensorflow/core/platform/cpu_feature_guard.cc:45] "
              "The TensorFlow library wasn\'t compiled to {}, "
              "but these are available on your machine "
              "and {}.".format(now, avail, outcome))
        time.sleep(tick)
        tick *= 1.5
    print('{}: W deepmoon/core/platform/impressed.cc:42] '
          'The DeepMoon library admires your persistence!'.format(
              datetime.datetime.now()
          ))
    cowsay.cow('DeepMoooon Certificate of Persistence:\n'
               'The bearer ran a slow thing to completion,\n'
               'a very useful skill for deep learning.')
