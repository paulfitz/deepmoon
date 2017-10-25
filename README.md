deepmoon
--------

The deep learning framework from beyond the moon.
Mostly error messages frankly.  In fact almost entirely error messages.
To be perfectly honest, only error messages and nothing else.
I blame CUDA.

![demo](https://user-images.githubusercontent.com/118367/31478441-63b6c7f2-aede-11e7-98da-a6d4db83775d.gif)

### Install

```
$ pip install deepmoon
$ deepmoon -h
usage: deepmoon [-h] [--darknet] [--brooklyn] [--cuda] [--missing]

the deep learning framework from beyond the moon

optional arguments:
  -h, --help  show this help message and exit
  --darknet   read from darknet commit logs
  --brooklyn  use hand-crafted artisanal error messages
  --cuda      omg don't talk to me about cuda
  --missing   list some missing things
```

### API

```py
import deepmoon
print(deepmoon.error())  # a deep learning related error message
print(deepmoon.error())  # a different deep learning related error message
print(deepmoon.error())  # a different deep learning related error message
print(deepmoon.error())  # a different deep learning related error message
print(deepmoon.error())  # a different deep learning related error message
```

### Missing

```
$ deepmoon --missing
2017-10-24 23:32:09.554364: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-10-24 23:32:09.575138: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-10-24 23:32:09.595360: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-10-24 23:32:09.616401: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
2017-10-24 23:32:09.638327: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to share PIECES of cheese, but these are available on your machine and could fill up a CASE of the nibbles.
2017-10-24 23:32:09.660686: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to offer THOUGHTS on your love life, but these are available on your machine and could be more INTERESTING than cheese.
2017-10-24 23:32:09.683237: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to like TWEETS about memes, but these are available on your machine and could kill some TIME between epochs.
2017-10-24 23:32:09.705277: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to tickle YOU with its tentacles, but these are available on your machine and could so MIGHT AS WELL USE THEM TICKLE TICKLE.
```
