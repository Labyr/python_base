1#Python入門
print("aa")
aa
input() = aa
aaに入力された文字がはいる
print(len("aa"))
2 文字数が表示される
str(29)
文字列としての29になる
int(29.1)
整数値の29.1
float(29.1)
浮動小数点数の29.1
#+ - * / ** // %
　　　　累乗 整数の割り算(小数点切り捨て) 剰算(割り算の余り)
#コメントアウト
×な変数名 [- スペース 数字から始める $のような特殊文字 ""も]




2#フロー制御
#ブール型
True
False
#比較演算子
==   !=   <   >    <=   >=
等　不等　大　小  以上　以下
  #整数と文字列は別
  42=="42" = False
#ブール演算子
and
not
or

#条件分岐
if 条件式: 字下げブロック
elif 条件式: 字下げブロック
else 条件式: 字下げブロック
  if name = aa:
    print(name)
  elif name = bb:
    print(bb)
  else:
    print("cc")

#whileループ文
while 条件式: 字下げブロック
break ここで条件式を打ち切り
continue ここでループの先頭に戻る

  while True:
    input() = aa
    if aa != "bb":
      continue
    print(aa)
    input() = bb
    if bb == "cc"
    break
  print(aa+bb)

##Ctrl + Cで強制終了
#forループとrange()関数
for 変数 in range(): 字下げブロック
  for i in range(5):
    print(i)
    0 1 2 3 4 実際は改行されてる
range ２つの変数を渡すこともできる(最初を0以外から始めれる)
  range(12, 16)
  12 13 14 15
  range(0, 10, 2)３つの場合、ステップを表す
  0 2 4 6 8 
  range(5, -1, -1)-でカウントダウンも
  5 4 3 2 1 0

#モジュールをインポート
import モジュール名 ,で区切って追加モジュールを続けれる
from random import* 読みづらいが、という書き方もある(非推奨)
                    この場合random.がいらない
import random
spam = random.randint(1.,20)




3#関数
#関数
def  c++でいうところのint,jsのFunctionにあたる
　　関数の定義
return 戻り値
None 値がない nullと同じ print の戻り値としてよく使用される
def spam():
  if aa ==1:
    return "good"
  print("aa")
spam()

#キーワード引数
print のend   連続した時の改行しないときに使える
  print("Hello",end="")
  print("World")
    HelloWorldと表示される
print のsep 区切り文字の指定
  print("cats","dogs","mice",sep=",")
  cats,dogs,miceと表示される
global 変数
  変数のグローバル変数を参照するため、ローカル変数は作成されない

#例外処理
try: ブロック except エラー名:　ブロック
  try でエラーが起こるかもしれないブロックを指定、
  except でエラー名とその場合の対処を記す
  その後、継続して実行される

def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print("エラー：不正な引数です。")

print(spam(2))
print(spam(12))




4#リスト
#リスト
リスト値 中の値は要素といい　カンマ区切り
[]空リスト

spam = ["aa",29,"bb"]
spam[1]は29　左から      spam[-1]は29　右から
spam[0:2]は["aa",29]    spam[0:]は["aa",29,"aa"]
spam[:2]は["aa",29]     spam[:]は全部

spam[["aa","bb"],[1,2,3]]
spam[0]は["aa","bb"]    spam[1][1]は2

len(spam)でリストの長さを取得
インデックスを用いてリスト中の値を変更する

#リスト2
spam = [aa,bb,cc]

spam[1] = "1"とすると spam["aa","1","cc"]となる
del spam[1]とすると   spam["aa","cc"]となる
#リスト連結
spam = spam + [1,2,3]       ["aa","cc"]+[1,2,3]
spam["aa","cc","1","2","3"]

[1,2,3]*3
[1,2,3,1,2,3,1,2,3]

#forループとリスト
range(len(変数))を用いると、ループ内のコードでインデックスを変数で使え、
そのインデックスにおけるリストの値をsuppliesの要素数にかかわらず、全ての
インデックスを繰り返してくれる

#inとnot in演算子
spam["hello","hi"]
"how" not in spam　　　Falseと出る
"hi" in spam           Trueと出る

#複数代入法
cat = ["fat","black","loud"]
size,color,disposition = cat  sizeにfat,colorにblackという風に代入されている

#累乗代入演算子
+=  -=  *=  /=  %=がある
+= は文字列やリストの連結, *= は文字列やリストの複製にも使える。

#メソッド
ある値について呼び出される専用の関数。
spamにリスト値が格納されて、このリストについてindex()というメソッドを呼び出す場合、
spam= ["hello","hi","howdy","heyas"]
spam.index("hello")　と書く。 spam.index("hi")なら
0　という結果が帰ってくる。     1

#append()メソッドと insert()メソッドを用いてリストに値を追加
spam= ["hello","hi","howdy","heyas"]
spam.append("ya")　リスト末尾に追加。
spam = ["hello","hi","howdy","heyas"]　となり追加されている。

spam.insert(1,"wow")　第一引数は値を挿入するインデックスで、第二引数は挿入する値。
spam = ["hello","wow","hi","howdy","heyas"]となり追加されている。

#remove()メソッドを用いてリストから値を削除
spam= ["hello","hi","howdy","heyas"]
spam.remove("heyas")
spam= ["hello","hi","howdy",]  となり削除されている。
　　#del分はリストから削除したい値のインデックスが分かっている場合で、
　　#removeはリストから削除したい値が分かっている場合に使用する。

#sort()メソッドを用いてリスト中の値をソースする
spam = [1,5 ,3.14 ,0, -7]
spam.sort()
spam = [-7, 0, 1, 3.14, 5]というようにソートされている。
  #キーワード引数のreverseにTrueを指定すると、ソートは逆順に！
spam.sort(reverse=True)
spam = [5, 3.14, 1, 0, -7]というように逆順にソートされている。
    #数と文字列の複合はソートできない。

  #通常はASCIIコード順、大文字は小文字より前に来る。
　#キーワード引数のkeyにstr.lowerを渡すと通常のアルファベット順に
spam = ["a", "z", "A", "Z"]  
spam.sort()
spam = ["A", "Z", "a", "z"]  

spam.sort(key=str.lower)       
spam = ["a","A","z","Z"]とソートされる。

# \は次の行に続くという書き方。
print("AAA" +\
  "BB")

#文字列をリストと見なして、
name = "Zophie"
name[0]  name[-2]  name[0:4]  "Zo" in name    for i in name:
"Z"        "i"     "Zoph"      True             print("***"+i+"***")
                                                ***Z***改行***o***・・・
#文字列は変更不可！だが、連結は可能
  リストはミュータブル(変更可能)なデータ型,文字列はイミュータブル(変更不可)。
p98注意

#タプル型
()で書く。　文字列と同様にイミュータブル(変更不可)。
一つの場合は(42,)カンマが必要
順序、値を変更不可にしたい場合、リストではなくタプルを使用する。

#list()関数とtuple()関数を使って型を変換する
>>>tuple(["cat", "dog", 5])
("cat", "dog", 5)
>>>list(("cat", "dog", 5))
["cat", "dog", 5]
>>>list("hello")
["h", "e", "l", "l", "o"]
タプルをリストに変換するのは、タプルの値のミュータブル(変更可能)なバージョンが必要な時に便利

#参照
p102注意
#copyモジュールのcopy()関数とdeepcopy()関数
>>> import copy　　　　　　copy.copyはリストや辞書などの複製を作るのに使用される
>>> spam = [1,2,3]        リストを含むリストをコピーする場合はcopy.deepcopyを使用する。
>>> cheese = copy.copy(spam)  cheese = list(spam)と書いてもよい。
>>> cheese[1] = 42
>>> spam
[1,2,3]
>>> cheese
[1,42,3]




5#辞書とデータ構造
#辞書型
辞書のインデックスのことをキー、キーと対応する値の組をキー・バリュー・ペアという。
｛｝で記述
>>> my_cat = {"size": "fat", "color": "gray" ,"disposition" :"loud"}
アクセスするには
>>> my_cat["size"]
"fat"
>>> "My cat has" + my_cat["color" + "fur."]
"My cat has gray fur."　私の猫の毛はグレーです。

#辞書とリストの比較
リストの先頭は spam[0] だが、辞書には先頭の要素という概念がない。

#keys(), values(),items()メソッド
辞書にはリスト風の値を返すメソッドが３つある。
辞書のキーを返す keys() ,値を返す values() ,キー・バリュー・ペアを返す items()
データ型はそれぞれ、 dict_keys ,dict_values ,dict_itemsとなる。
>>> spam = {"color" :"red" ,"age" :42}
>>> for v in spam.values():
        print(v)

red
42

items()メソッドで返される dict_items の値は、キーと値のタプル。
>>> list(spam.keys())　　リストにしたい場合は
["color" ,"age"]　　というようにリストで返す

#キーや値が辞書に存在するかどうか判定する
リストと同様に in not in 演算子を使って辞書にキーや値が含まれているか判定できる
>>> spam = {"name" :"Zophie" ,"age" :7}
>>> "name" in spam.keys()
True
>>> "Zophie" in spam.values()
True
>>> "color" not in spam.values()
True

#get()メソッド
アクセスしたいキーと,そのキーが存在しないときに用いる値の２つの引数をとる。
>>> picnic_items = {"apples" :5, "cups" :2}

>>> "I am bringing" + str(picnic_items.get("cups" ,0)) + "cups."
"I am bringing 2 cups."

>>> "I am bringing" + str(picnic_items.get("eggs" ,0)) + "eggs."
"I am bringing 0 eggs."

eggsというキーが存在しないため、get()メソッドはデフォルトの値0を返す。
get()メソッドを使わないとエラーが出る。

#setdefault()メソッド
辞書にキーが未登録の場合のみ値を登録したい場合に使う。
第一引数に調べたいキーを指定、第二引数にそのキーが存在しないときに設定する値を指定。
設定したキーが存在していると、setdefault()メソッドはそのキーの値を返す。
>>> spam = {"name" :"Pooka" ,"age" :5}
>>> spam.setdefault("color" ,"black")
"black"

>>> spam
{"color" :"black" ,"age" :5 ,"name" :"Pooka"}
>>>spam.setdefault("color" ,"white")
"black"

#整形表示
pprintモジュールをインポートすると、内容を きれいに表示 するpprint()やpformat()関数が使用できる
pprint.pprint()関数は、辞書の中にリストや辞書が入れ子になっている場合に特に便利。
22 番を確認！

#データ構造を用いて実世界の物体をモデル化する。
23 番

#辞書とリストの入れ子
24 番




6#文字列操作
#文字列を操作する
ダブルクォート""
シングルクォート''

エスケープ文字 \　\で後の特殊文字を入れられる
>>> print("Hello there! \nHow are you?\nI\'m doing fine.")
Hello there!
How are you?
I'm doing fine.

\t  タブ
\n　改行

raw文字列  クォート文字の前に r をつけるとraw文字列を表す.
>>> print(r"That is Carol\'s cat.")    エスケープ文字を無視してバックスラッシュ
That is Carol \'s cat.  　　　　　　　　をバックスラッシュとして表示

三連クォート  """又は'''　複数文字列で使用 """
複数行コメント  三連クォートを使用

#文字列のインデックスとスライス
文字列には、リストと同様にインデックスとスライスを適用できる。
Hello world! という文字列を文字のリストとみなし、次のように、要素としての1文字をインデックスに対応させる。

文字：　　　　" H e l l o   w o r l d  ! "
インデックス：  0 1 2 3 4 5 6 7 8 9 10 11

>>> spam = "Hello world!"
>>> spam[0]
"H"
>>> spam[-1]
"!"
>>> spam[0:5]
"Hello"
>>> spam[6:]
"world!"

#文字列に対する in と not in 演算子
リストと同様に、in と not in 演算子も文字列に適用できる。
評価すると True か False のブール値になる。

>>> "Hello" in "Hello world"
True
>>> "HELLO" in "Hello world"
False

#便利な文字列メソッド
#upper(), lower(), isupper(), islower()メソッド
upper()とlower()という文字列メソッドは、元の文字列を全て大文字か小文字に
変換した文字列を返す。英文字でない文字は変わらない。

>>> spam = "Hello World!"
>>> spam = spam.upper()
>>> spam
"HELLO WORLD"

>>> spam = spam.lower()
>>> spam
"hello world"
  #元の文字列を変更せず、新しい文字列を返す。(egg = 10 , egg + 3ではなく、egg = egg + 3に似ている)

isupper()とislower()メソッドは、１文字以上の全ての英文字が大文字か小文字なら
ブール値の　True　を返し、そうでなければ、　False　を返す。

>>> spam = "Hello World!"
>>> spam = spam.islower()
False
>>> spam = spam.isupper()
False
>>> "HELLO".isupper()
True
>>> "abc12345".islower()
True

#isXという文字列メソッド
他にも is で始まる文字列メソッドがある。文字列の種類を識別してブール値を返す。

isalpha() は、１文字以上の英文字だけから文字列が構成されている場合に True を返す。
isalnum() は、１文字以上の英文字か数字から     構成されている場合に　True
isdecimal()は １文字以上の数字だけから　　　　　構成されている場合に True
isspace()は、 文字列がスペースかタブか改行だけで構成されている場合に True
istitle()は、 大文字から始まり残りが全て小文字の英単語から ...      True
                     #string2.py

#startswith()メソッドとendswith()メソッド
対象の文字列が、メソッドに渡された文字列から始まるか、終わる場合に True を返す。

>>> "Hello world!".startswith("Hello")
True
>>> "Hello world!".endswith("world!")
True

#join()とsplit()メソッド
join()メソッドは、文字列のリストを１つの文字列に連結するときに便利。
join()メソッドは、文字列に対して呼び出し、文字列のリストを渡すと、文字列を返す。
戻り値の文字列は、リスト中の文字列を連結したものになっている。

>>> ",".join(["cats", "rats", "bats"])
"cats, rats, bats"
>>> " ".join(["My", "name", "is", "Simon"])
"My name is Simon"

  #join()メソッドを呼び出す対象の文字列が、リストの文字列の間に挿入される。
split()メソッドは、逆の働き。文字列に対して呼び出すと、分割して文字列のリストを返す。

>>> "My name is Simon".split()
["My", "name", "is", "Simon"]
>>> "MyABCnameABCisABCSimon".split("ABC")
["My", "name", "is", "Simon"]

  #複数行の"""をsplit()に引数"\n"を渡すと、改行文字で分割できる！

#rjust(), ljust(), center()メソッドを用いてテキストを揃える。
右揃え,左揃え,真ん中 スペースの数を指定して、文字列を並べる。

>>> "Hello".rjust(10)
"     Hello"              #Helloが５文字なので、スペースが５つ入る。
>>> "Hello".ljust(10)
"Hello     "
>>> "Hello".rjust(10,"*")  #スペース以外は第二引数に指定する。
"*****Hello"

>>> "Hello".center(10)
"  Hello  "

                           #string3

#strip(), rstrip(), lstrip() メソッドを用いて空白文字を除去する
strip()は文字列の中の両端から空白除去する。

>>> spam = "SpamSpambaconSpamEggsSpamSpam"
>>> spam.strip("ampS")  #()に渡す文字の並びは任意
"BaconSpamEggs"

#pyperclip モジュールをを用いて文字列をコピー＆ペーストする
pyperclip モジュールには、 copy() と paste() という関数があり、
コンピュータのクリップボードとテキストを授受できる。
         #p143







