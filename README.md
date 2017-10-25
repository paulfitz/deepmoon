deepmoon
--------

The deep learning framework from beyond the moon.
Mostly error messages frankly.  In fact almost entirely error messages.
To be perfectly honest, only error messages and nothing else.
I blame CUDA.

![demo](https://user-images.githubusercontent.com/118367/31478441-63b6c7f2-aede-11e7-98da-a6d4db83775d.gif)

## Install

```
$ pip install deepmoon
$ deepmoon -h
usage: deepmoon [-h] [--darknet] [--brooklyn]

the deep learning framework from beyond the moon

optional arguments:
  -h, --help  show this help message and exit
  --darknet   read from darknet commit logs
  --brooklyn  use hand-crafted artisanal error messages
```


```py
import deepmoon
print(deepmoon.error())  # a deep learning related error message
print(deepmoon.error())  # a different deep learning related error message
print(deepmoon.error())  # a different deep learning related error message
print(deepmoon.error())  # a different deep learning related error message
print(deepmoon.error())  # a different deep learning related error message
```
