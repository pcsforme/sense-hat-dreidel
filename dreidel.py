from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()

w = (0, 0, 0)
l = (200, 200, 200)
b = (0, 70, 150)

nun = [
    w, w, w, b, b, w, w, w,
    w, w, w, b, b, w, w, w,
    b, b, l, l, l, b, b, b,
    b, b, b, b, l, b, b, b,
    b, b, b, b, l, b, b, b,
    b, b, b, b, l, b, b, b,
    w, b, l, l, l, b, b, w,
    w, w, w, b, b, w, w, w,
]

gimmel = [
    w, w, w, b, b, w, w, w,
    w, w, w, b, b, w, w, w,
    b, b, l, l, l, b, b, b,
    b, b, b, b, l, b, b, b,
    b, b, b, b, l, b, b, b,
    b, b, b, l, l, b, b, b,
    w, b, l, b, l, b, b, w,
    w, w, w, b, b, w, w, w,
]

hey = [
    w, w, w, b, b, w, w, w,
    w, w, w, b, b, w, w, w,
    b, b, l, l, l, l, b, b,
    b, b, b, b, b, l, b, b,
    b, b, l, b, b, l, b, b,
    b, b, l, b, b, l, b, b,
    w, b, l, b, b, l, b, w,
    w, w, w, b, b, w, w, w,
]

shin = [
    w, w, w, b, b, w, w, w,
    w, w, w, b, b, w, w, w,
    b, l, b, l, b, l, b, b,
    b, l, b, l, b, l, b, b,
    b, l, b, l, b, l, b, b,
    b, l, b, l, b, l, b, b,
    w, l, l, l, l, l, b, w,
    w, w, w, b, b, w, w, w,
]

display_letters = [nun, gimmel, hey, shin]

while True:
    x, y, z = sense.get_accelerometer_raw().values()
    x = abs(x)
    y = abs(y)
    z = abs(z)
    if x > 2 or y > 2 or z > 2:
        for a in range(10):
            sense.set_pixels(nun)
            sleep(.07)
            sense.set_pixels(gimmel)
            sleep(.07)
            sense.set_pixels(hey)
            sleep(.07)
            sense.set_pixels(shin)
            sleep(.07)
        result = random.choice(display_letters)
        sense.set_pixels(result)
