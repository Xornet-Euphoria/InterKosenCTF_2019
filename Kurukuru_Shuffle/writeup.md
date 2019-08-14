# KuruKuru Shuffle

| score | genre  |
| ----  | ----   |
| 200	| Crypto |


## 添付ファイル
- `shuffle.py`: 暗号化する際のソースコード
- `encrypted`: 暗号化されたファイル

## 方針
3つのパラメータ`a, b, k`によって文字数回分の転置規則(何回目にどの文字とどの文字を転置するか)が定まり、全通り考えたとしても高々10万通りとちょっと。よって総当りが可能であると考えられる。

## 手順
1. 各パラメータ毎にどの文字とどの文字を何回目で置換するかを配列で格納する
2. 各転置規則に対してそれを逆順に実行して復号を行う
3. 復号結果に`KosenCTF{`を含むかを確認する

## 使用コード
```python
 from copy import copy
 
 
 def make_st_list(a, b, k, L):
     _list = []
     i = k
     for _ in range(L):
         s = (i + a) % L
         t = (i + b) % L
         i = (i + k) % L
         _list.append([s, t])
 
     return _list
 
 
 def dec(_enc_list, _st_list):
     for _ in range(len(_st_list)):
         st = _st_list.pop()
         s = st[0]
         t = st[1]
         _enc_list[s], _enc_list[t] = _enc_list[t], _enc_list[s]
 
     return "".join(_enc_list)
 
 
 if __name__ == '__main__':
     enc = "1m__s4sk_s3np41m1r_836lly_cut3_34799u14}1osenCTF{5sKm"
     L = len(enc)
 
     enc_list = list(enc)
 
     for a in range(L):
         for b in range(L):
             for k in range(1, L):
                 st_list = make_st_list(a, b, k, L)
                 tmp_enc_list = copy(enc_list)
                 dec_str = dec(tmp_enc_list, st_list)
                 if dec_str[0:9] == "KosenCTF{":
                     print(dec_str)
```

## Flag
KosenCTF{us4m1m1_m4sk_s3np41_1s_r34lly_cut3_38769915}
