# Lost World

| score	| genre |
| ----  | ----  |
| 303	| Forensics |

## 添付ファイル
- ディスクイメージ(.vdi)

## 方針
vdiを渡されそれをVirtualbox等で読み込ませるとログインパスワードを要求される。ログインパスワード自体を入手するのは骨が折れそうなので内部の暗号化されたログイン情報が入っている`/etc/shadow`を書き換えてログインできるようにする

## 手順
1. 下記参考文献に従って`root:`でヒットする箇所をこちらで用意した鍵に置き換える(今回は下記参考文献の物を流用したが、皆さんがお使いのLinuxの`/etc/shadow`を流用して問題ないと思われる)
2. VirtualBoxで書き換え後のイメージを読み込み、起動
3. 用意したパスワードを入力し`dmesg | grep KosenCTF{`をしてフラグを入手

## Flag
KosenCTF{u_c4n_r3s3t_r00t_p4ssw0rd_1n_VM}

## 参考文献
write-ups/Hack.lu CTF 2015/Dr.Bob
https://github.com/RandomsCTF/write-ups/tree/master/Hack.lu%20CTF%202015/Dr.%20Bob%20%5Bforensics%5D%20(150)
