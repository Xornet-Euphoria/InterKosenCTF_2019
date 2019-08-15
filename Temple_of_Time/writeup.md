Temple of Time

| score	| genre |
| ----  | ----  |
| 285	| Forensics, Web |

## 添付ファイル
- pcapng

## 方針
パケットを解析するとどうやらSQLインジェクションの痕跡が見える。それもTime-BasedのブラインドSQLインジェクションだと思われる。攻撃者は1文字ずつ情報を探索しているので調査している文字が切り替わったタイミングのパケットを読めば攻撃者が判明させた文字がわかる。

## 手順
1. Wiresharkにpcapngを読ませ、プロトコルをHTTPに絞る
2. `GET /index.php?portal=%27OR%28SELECT%28IF%28ORD%28SUBSTR%28%28SELECT+password+FROM+Users+WHERE+username%3D%27admin%27%29%2C1%2C1%29%29%3D48%2CSLEEP%281%29%2C%27%27%29%29%29%23 HTTP/1.1 `というリクエストからTime-Based SQL injectionを行っているように思われる  
なお、これをデコードすると
`GET /index.php?portal='OR(SELECT(IF(ORD(SUBSTR((SELECT+password+FROM+Users+WHERE+username='admin'),1,1))=48,SLEEP(1),'')))# HTTP/1.1 `
であることからこれは1文字目が文字コードで48('0')であるかを判定していると思われる
3. 該当パケットを解析しやすいようにCSV形式で出力する
4. `IF`の条件は`username`が`admin`のレコードの`password`のある位置の文字コードがn(上記例では48)であるかであり、このnをパケットを送るごとに1ずつ変化させている
5. `SUBSTR`の引数に注目するとあるパケットとパケットの間で引数が変わっているが、この代わり目である位置の文字コードが判明したことになるのでそこのパケットを抽出する
6. 抽出したパケットから文字コードの部分を読んで文字に戻し、繋げるとフラグが現れる

## 使用コード
ここでは5. の抽出だけ行いフラグの復旧は人力で行ったので割愛、6.も自動化した方がWriteupとして見栄えが良かったと反省
```python
import csv
 
if __name__ == '__main__':
    payloads = []
    with open('export.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            payload = row[6]
            if payload[0:10] == "GET /index":
                payloads.append(payload)
 
    index = 1
    for j, payload in enumerate(payloads):
        search_word = "GET /index.php?portal=%27OR%28SELECT%28IF%28ORD%28SUBSTR%28%28SELECT+password+FROM+Users+WHERE+username%3D%27admin%27%29%2C" + str(index)
        if search_word not in payload:
            print(payloads[j - 1])
            index += 1
```

## Flag
KosenCTF{t1m3_b4s3d_4tt4ck_v31ls_1t}
