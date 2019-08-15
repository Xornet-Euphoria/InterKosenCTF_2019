## saferm

| score	| genre |
| ----  | ----  |
| 434	| Forensics, Reversing |


## 添付ファイル
- ディスクダンプ

## 手順
1. FTK Imagerにこのイメージを読ませると`saferm`というバイナリと削除された`document.zip`というファイルが見つかる
2. `saferm`をリバーシングすると(ここはチームメイトがやってくれた、感謝)、64bitのキーを用いて暗号化`(encrypted[index] = file[index] ^ key[index % 64])`してから元のファイルを削除していることがわかる。
3. FTK Imagerは削除済みのファイルも吸い出せるので唯一削除済みと表示されたファイルである`document.zip`を抽出する。
4. ここでzipファイルのシグネチャは頭4バイトは確定しており残りの4バイトもバージョン情報(単にdeflate圧縮であれば`14 00`)と圧縮形式ごとに用いる特殊ビット(特にオプション指定が無ければ`00 00`)であることから容易に候補を絞ることができる  
※この候補を絞る過程ではファイル名が`document.pdf`であるという仮定も用いた
5. これにより幾つかキーの候補を絞り復号化を行うとあるキーでzipが開くことができ、中に入っていた`document.pdf`を見るとフラグが(但し、手元のアーカイバでは開かずチームメイトが使っているツールでは開くことができた、感謝)  
※公式Writeupによれば暗号化の際、末尾の64bitに満たない部分は暗号化されないのでここだけ元のバイト列のままで良いらしい

## 使用コード
過去に出場したCTFでXORによる暗号化を実装していたので(https://github.com/Xornet-Euphoria/HSCTF_6/tree/master/Hidden_Flag)キーを変えて流用
```python
if __name__ == '__main__':
    key = [46, 87, 173, 46, 255, 200, 202, 73]
    f = open('document.zip', 'rb')
    enc_bytes = f.read()
    f.close()

    f = open('dec.zip', 'wb')
    for i, byte in enumerate(enc_bytes):
        f.write((int(byte) ^ key[i % len(key)]).to_bytes(1, 'big'))

    f.close()
```

## Flag
KosenCTF{p00r_shr3dd3r}
