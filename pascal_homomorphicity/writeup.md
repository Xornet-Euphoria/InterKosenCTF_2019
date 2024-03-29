# pascal homomorphicity

| score	| genre |
| ----  | ----  |
| 333	| Crypto |


## 添付ファイル
- サーバー側で動いてるコード

## 方針
※GitHubに数式貼るには画像を貼る等の方法になりますがめんどくさいので下記のような雑な書き方をしています  
二項定理より`(1+n)^k \equiv 1 + kn \mod n^2`であることがわかる。これを使えば`1 + kn < n^2`である時に`(1+n)^k`と`n`がわかっていれば`k`を求めることができる(逆も同様)。  
今回のプログラムではサーバー側に小さい数字を渡すと、警告と共に`key`の長さを教えてくれて、`key < n`であったことから`1 + kn < n^2`の条件が適用されるので剰余を考慮しなくても解くことができる。

## 手順
1. 鯖に接続すると`pow(1 + n, key, n**2) `が表示される
2. 数値を入力すると`pow(1 + n, int(input), n**2)`が表示されるので`(1+n)^k \equiv 1 + kn \mod n^2`を利用し`n`を導出する
3. `n`が求まったので最初に表示された`pow(1 + n, key, n**2)`から`key`を導出できる

当然ながらPythonを利用して解きましたがPythonターミナル上で全てを行ったので使用コードはありません。

## Flag
KosenCTF{Th15_15_t00_we4k_p41ll1er_crypt05y5tem}

## 参考文献
- Paillier暗号 - Wikipedia: https://ja.wikipedia.org/wiki/Paillier%E6%9A%97%E5%8F%B7