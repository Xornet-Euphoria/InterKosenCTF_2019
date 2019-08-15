# Hugtto! (InterKosenCTF)

| score | genre |
| ----  | ----  | 
| 238   | Forensics |

## 添付ファイル
- `steg.py`: steganographyを行うファイル
- `steg_emiru.png`: steg.pyによって生成された画像ファイル

## 手順
1. 乱数によって画素のどの色に情報を仕込むか決まるがその仕込み方は
`r = (r & 0xFE) | bin_flag[i % len(bin_flag)]`
のように一定(`r`は赤色、`g`は緑色、`b`は青色に関する値が入っている)
2. ここで8bit整数と`0xFE`の論理積を取るとこの整数は末尾1桁が0になる。
3. また、`bin_flag[i]`は`0`か`1`であるので上記値は`0|0 = 0`か`0|1 = 1`となり`bin_flag[i]`の値に依存する
4. 従ってどの色に仕込まれたのかさえ判明すれば`bin_flag[i]`の値を復元可能。復元方法は単純に色の値の最下位ビットの偶奇である
5. `random.seed(int(datetime.now().timestamp()))`よりこのファイルが作られる直前の時刻をシードとして乱数を生成していることからファイル生成時刻のUNIX時間、`int(datetime(2019, 8, 6, 11, 44, 18).timestamp())`からこれより少し小さい値をシードとして乱数を生成するとこのファイルが作られた時と同じ埋め込み方が可能だと考えられる
6. 1秒ずつ早い時間にしていったところ3秒早い時刻で復号したところフラグのようなものが表示された

```python
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
```
 

## Flag
KosenCTF{Her_name_is_EMIRU_AISAKI_who_is_appeared_in_Hugtto!PreCure}
