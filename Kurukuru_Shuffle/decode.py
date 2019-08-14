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
