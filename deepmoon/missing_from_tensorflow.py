
import datetime
import time


def list_missing_things():

    acts = [
        ('use SSE4.2 instructions', 'speed up CPU computations'),
        ('use AVX instructions', 'speed up CPU computations'),
        ('use AVX2 instructions', 'speed up CPU computations'),
        ('use FMA instructions', 'speed up CPU computations'),
        ('share PIECES of cheese', 'fill up a CASE of the nibbles'),
        ('offer THOUGHTS on your love life',
         'be more INTERESTING than cheese'),
        ('like TWEETS about memes', 'kill some TIME between epochs'),
        ('tickle YOU with its tentacles',
         'so MIGHT AS WELL USE THEM TICKLE TICKLE')
    ]

    for avail, outcome in acts:
        now = datetime.datetime.now()
        print("{}: W tensorflow/core/platform/cpu_feature_guard.cc:45] "
              "The TensorFlow library wasn\'t compiled to {}, "
              "but these are available on your machine "
              "and could {}.".format(now, avail, outcome))
        time.sleep(0.02)
