from PIL import Image
from datetime import datetime
import random


def bit_array_to_string(bit_array):
    try:
        if len(bit_array) != 8:
            raise ValueError("argument 'bit_array' must be 8 length" )
    except ValueError as e:
        print(e)

    bit_str = "".join(list(map(str, bit_array)))
    return chr(int(bit_str, 2))


if __name__ == '__main__':
    img = Image.open("./steg_emiru.png")
    new_img = Image.new("RGB", img.size)

    w, h = img.size
    # 誤差が1sぐらいあるかもしれない
    seed_time = int(datetime(2019, 8, 6, 11, 44, 15).timestamp())
    print(seed_time)
    random.seed(seed_time)
    # rnd_array = [random.randint(0, 2) for _ in range(w * h)]

    i = 0
    bit_array = []
    current_bit_array = []
    for x in range(w):
        for y in range(h):
            r, g, b = img.getpixel((x, y))
            rnd = random.randint(0, 2)
            if rnd == 0:
                current_bit_array.append(r % 2)
            elif rnd == 1:
                current_bit_array.append(g % 2)
            elif rnd == 2:
                current_bit_array.append(b % 2)
            i += 1
            if i % 8 == 0:
                bit_array.append(current_bit_array)
                current_bit_array = []

    str_arr = []
    for i, arr in enumerate(bit_array):
        if i < 100:
            str_arr.append(bit_array_to_string(list(reversed(arr))))

    print("".join(str_arr))
