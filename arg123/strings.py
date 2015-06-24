#!/usr/bin/env python
# coding:utf-8
"""文字列操作をひとととり
たぶん日本語はuを付けてunicodeとして取り扱ったほうが無難
付けないと文字の場所が何バイト目かで取り扱われるっぽい"""


if __name__ == "__main__":
    str = "abcdefgABCDEFG";
    str2 = u"あいうえおアイウエオ"
    str3 = u"abcdefgあいうえお"
    str4 = u"あいうえおabcdefg"
    str5 = "あいうえおabcdefg"
    str6 = u"ああああ\tい いい\tううう"
    str7 = "this is a pen."

    #表示系
    def strings_print():
        print str      # abcdefgABCDEFG
        print str[3:5] # de             3文字目より後5文字目の前まで
        print str[:4]  # abcd           4文字目の前まで
        print str[5:]  # fgABCDEFG      5文字目より後
        print str[:-1] # abcdefgABCDEF　最後から1文字前まで

    #len()で文字列長さの取得
    def getlen():
        print "■len()で文字列長さの取得"
        print len(str)  # 14
        print len(str2) # 10 uを付けるとunicodeで文字数を返却する
        print len(str5) # 30 uを付けずに定義したするとutf-8にエンコードされてバイト数が返却される

    #大文字小文字の操作
    def lower_upper():
        print "■大文字小文字の操作"
        #lower:小文字に変換
        print str.lower()                   # abcdefgABCDEFG
        print u"ＡＢＣ".lower()             # ａｂｃ
        #upper:大文字に変換
        print str.upper()                   # ABCDEFGABCDEFG
        print u"ａｂｃ".upper()             # ＡＢＣ
        print str3.upper()                  # ABCDEFGあいうえお
        #swapcase:大文字と小文字を入れ替える
        print str.swapcase()                # ABCDEFGabcdefg
        print u"ａｂｃＡＢＣ".swapcase()    # ＡＢＣａｂｃ
        #capitalize:最初の文字列のみを大文字にした文字列のコピーを返却
        print str.capitalize()              # Abcdefgabcdefg
        print str2.capitalize()             # あいうえおアイウエオ(変化なし)
        print str3.capitalize()             # Abcdefgあいうえお
        print str4.capitalize()             # あいうえおabcdefg(変化なし)
        print str7.capitalize()             # This is a pen.
        # title:タイトルケースにする
        print str7.title()                  # This Is A Pen. 用途がわからん

    #文字列整形
    def strings_shape():
        print "■文字列整形"
        #ljust:左寄せ
        print "12345" + "aaa"                    # 12345aaa
        print "12345".ljust(10) + "aaa"          # 12345     aaa
        print "12345".ljust(10,"_") + "aaa"      # 12345_____aaa
        print u"あああ".ljust(5) + "aaa"         # あああ  aaa(全角も文字として数えられる)
        print u"あああ".ljust(5,u"＿") + "aaa"   # あああ＿＿aaa(埋め文字を全角にするといい感じ)
        #rjust:右寄せ
        print "aaa" + "12345"                    # aaa12345
        print "aaa" + "12345".rjust(10)          # aaa     12345
        print "aaa" + "12345".rjust(10,"_")      # aaa_____12345
        print "aaa" + u"あああ".rjust(5)         # aaa  あああ(全角も文字として数えられる)
        print "aaa" + u"あああ".ljust(5,u"＿")   # aaa＿＿あああ(埋め文字を全角にするといい感じ)
        #center:中央寄せ
        print "#" * 20
        print str.center(20)                     # 中央に寄る
        print "#" * 20
        print "#" * 25
        print str.center(25)                     # 割り切れないときは一つ後ろにずれる
        print "#" * 25
        print u"＃" * 20
        print str2.center(20)                    # マルチバイトは自身は1文字ずつカウントされるが前後の詰めが半角になるためうまく寄せられない
        print u"＃" * 20
        print str2.center(20,u"　")              # 第二引数にfillcharを指定することでちゃんと寄る
        print u"＃" * 20
        #lstrip:先頭のトリミング
        print "   hoge".lstrip()                 # hoge        何も指定しないと空白をトリミング
        print u"　hoge".lstrip()                 # hoge        何も指定しないと空白をトリミング(全角)
        print "# www.yahoo.co.jp".lstrip(".w# ") # yahoo.co.jp 先頭の"."とwと#と" "をトリミング
        #rstrip:最後のトリミング
        print len("hoge    ")                    # 8              トリミング前
        print len("hoge   ".rstrip())            # 4              何も指定しないと空白をトリミング
        print len(u"hoge　")                     # 5              トリミング前
        print len(u"hoge　".rstrip())            # 4              何も指定しないと空白をトリミング(全角)
        print "# www.yahoo.co.jp".rstrip("jp.")  # # www.yahoo.co 先頭のjとpと"."をトリミング
        #zfill:ゼロ埋め
        print "123".zfill(10)                    # 0000000123

    #文字列検索等
    def strings_find():
        print "■文字列検索等"
        #count:出現回数を数える
        print str.count("bcd")                           # 1
        print str.lower().count("bcd")                   # 2 abcdefgabcdefgが検索対象
        print str2.count(u"い")                          # 1
        print str.lower().count("bcd",0,str.find("A"))   # 1 abcdefgが検索対象 第二第三引数にstartとendを入れられる
        #find:文字列検索し、最初に見つかった最初の文字のsuffixを返す
        print str.find("c")                              # 2
        print str.find("cde")                            # 2
        print str.find("x")                              # -1 見つからない場合は-1を返却
        print str.lower().count("c")                     # 複数ある時は
        print str.lower().find("c")                      # 最初のものだけ
        print str.lower().find("c",3,len(str))           # 9 第二第三引数にstart/endが指定できるが返却されるsuffixは元の文字列のもの
        #rfind:複数回出現する場合に一番最後に出現する文字列のsuffixを返すfindのようなもの
        print str.lower().count("c")                     # 2
        print str.lower().find("c")                      # 2
        print str.lower().find("c")                      # 9
        #index:findと一緒だが見つからない場合にValueErrorを返却
        def tryindex(str,substr):
            try:
                return str.index(substr)
            except ValueError:
                return "ValueError occured"
        print tryindex(str,"c")                          # 2
        print tryindex(str,"x")                          # ValueError occured
        #rindex:findに対するrfindと同じ(index版)
        def tryrindex(str,substr):
            try:
                return str.index(substr)
            except ValueError:
                return "ValueError occured"
        print tryindex(str.lower(),"c")                  # 9
        print tryindex(str.lower(),"x")                  # ValueError occured
        #startswith:指定の文字列ではじまるときにTrueを返却
        print str.startswith("ab")                       # True
        print str.startswith("AB")                       # False
        tuple = ("ab","AB")
        print str.startswith(tuple)                      # True タプルも受け付けるよう
        print str.startswith("A",str.find("A"),len(str)) # True 第二第三引数でstart/endも指定可能
        #endswith:指定の文字列で終わるときにTrueを返却
        print str.endswith("fg")                         # False
        print str.endswith("FG")                         # True
        tuple = ("fg","FG")
        print str.endswith(tuple)                        # True タプルも受け付ける
        print str.endswith("g",0,str.find("A"))          # True 第二第三引数でstart/endも指定可能

    #エンコードデコード
    def enc_dec():
        print "■エンコードデコード"
        #encode:文字コードをエンコードする
        print u"以下はSJISのため文字化けします"
        print str2.encode("shift_jis")                     # 出力が混在するとうまくいかないけどこれで合ってる
        #decode:エンコードされた文字列をデフォルトの文字列エンコードにデコードする
        print str2.encode("shift_jis").decode("shift_jis") # あいうえおアイウエオ

    #文字列置換系
    def strings_replace():
        print "■文字列置換系"
        #replace:文字列置換
        print "abcabcabc".replace("c","x")   # abxabxabx
        print "abcabcabc".replace("c","x",2) # abxabxabc 第2引数で最初から何個分を置換するか決められる
        print "abcabcabc".replace("c","x",0) # abcabcabc 第2引数で0をしてみた 意味はないが痴漢はしない	
        #expandtabs:タブを半角スペースに置換する
        def hoge(str):
            """タブや半角スペースを見やすく置換する"""
            str = str.replace("\t","[tab]")
            str = str.replace(" ","[space]")
            return str
        print hoge(str6)                     # Tabを含む文字列
        print hoge(str6.expandtabs(8))       # Tabが半角スペースに置換されるタブ間隔は8文字
        #translate:mapを使って置換する
        import string
        map =  string.maketrans("abcABC","XYZxyz") # a->X b->Y c->Z A->x B->y C->zのつもり
        print str.translate(map)             # XYZdefgxyzDEFG
        print str.translate(map,"cde")       # XYfgxyzDEFG 第2引数を取り払ってから変換される

    #文字列分割
    def strings_separate():
        print "■文字列分割"
        #split:デリミタで分割してリストを返す(分割回数の指定は前から)
        print "dog:cat".split(":")            # ["dog", "cat"]
        print "dog:cat:mouse".split(":")      # ["dog", "cat", "mouse"]
        print "dog:cat:mouse".split(":",1)    # ["dog", "cat:mouse"]        第2引数で先頭から何回分割するか指定可能
        print "dog::cat:mouse".split(":")     # ["dog", "", "cat", "mouse"] 連続するデリミタは空文字が入っていると判断される
        print ":dog:cat:mouse".split(":")     # ["", "dog", "cat", "mouse"] 先頭にあるデリミタはその前に空文字があると判断される
        print "dog cat mouse".split()         # ["dog", "cat", "mouse"]     デリミタを指定しないと空白がデリミタとなる
        print "dog\tcat\tmouse".split()       # ["dog", "cat", "mouse"]     Tabも空白扱い
        print u"dog　cat　mouse".split()      # [u"dog", u"cat", u"mouse"]  全角スペースも同じような動き
        print "dog  cat mouse".split()        # ["dog", "cat", "mouse"]     デリミタを指定しない場合は連続するデリミタは空文字が入っているとは判断されない
        print " dog cat mouse".split()        # ["dog", "cat", "mouse"]     デリミタを指定しない場合は先頭の空白は無視される
        print "dog  cat mouse".split(" ")     # ["dog", "", "cat", "mouse"] 判断させるには明示的にデリミタを指定する
        print "dog cat mouse".split(None)     # ["dog", "cat", "mouse"]     デリミタにNoneを指定するのは指定しないのと同じ
        print "dog  cat mouse".split(None)    # ["dog", "cat", "mouse"]     デリミタにNoneを指定するのは指定しないのと同じ
        #rsplit:デリミタで分割してリストを返す(分割回数の指定は後ろから)
        print "dog:cat".rsplit(":")           # ["dog", "cat"]
        print "dog:cat:mouse".rsplit(":")     # ["dog", "cat", "mouse"]
        print "dog:cat:mouse".rsplit(":",1)   # ["dog:cat", "mouse"] 第2引数で最後から何回分割するか指定可能
        #splitlines:行で分割してリストを返す
        lines = "Hi, my name is Ken Ikeda.\nHi, my name is Yumi Okada\nHow are you?\nFine thank you.\nHow are you?\nI'm fine too."
        print lines.splitlines()              # ["Hi, my name is Ken Ikeda.", "Hi, my name is Yumi Okada", "How are you?", "Fine thank you.", "How are you?", "I'm fine too."]
        print lines.splitlines(True)          # ["Hi, my name is Ken Ikeda.\n", "Hi, my name is Yumi Okada\n", "How are you?\n", "Fine thank you.\n", "How are you?\n", "I'm fine too."] 第2引数をTrueとすると改行コードが残る(デフォルトはFalse)
        #partition:デリミタで分割してタプルを返却する
        print "dog:cat".partition(":")        # ("dog", ":", "cat)        デリミタを含む3つの要素のタプルに分割される
        print "dog:cat:mouse".partition(":")  # ("dog", ":", "cat:mouse") 複数のデリミタを含む場合は最初だけ分割される	
        #rpartition:デリミタで分割してタプルを返却する(後ろから探す)
        print "dog:cat".rpartition(":")       # ("dog", ":", "cat)        デリミタを含む3つの要素のタプルに分割される
        print "dog:cat:mouse".rpartition(":") # ("dog:cat", ":", "mouse") 複数のデリミタを含む場合は最後だけ分割される	

    #文字列書式(formatの世界)
    def strings_format():
        print "■文字列書式(formatの世界)"
        _str = "I am {0} years old."
        print _str.format(17)                             # 数字で指定すると順番に置き換わる
        _str = "My name is {0}. I am {1} years old."
        print _str.format("Taro","4")                     # リストで指定
        _str = "My name is {name}. I am {age} years old."
        print _str.format(name="Ken", age="21")           # キーワード引数で指定
        _dat = {"name":"Mike", "age":45}
        print _str.format(**_dat)                        # ディクショナリで指定もできる
        """たぶんもっと奥は深い"""
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
        _str = "My name is {0.name}. I am {0.age} years old."
        p = Person("Tadashi",6)
        print _str.format(p)
        """たぶんもっともっと奥は深い"""
        """要勉強"""

    #バリデーション
    def valid():
        print "■バリデーション"
        #isalpha:英字のみでTrue
        print "abc123".isalpha()  # False 
        print "abcdef".isalpha()  # True
        print "abc_ef".isalpha()  # False
        print u"ＡＢＣ".isalpha() # True 全角もいけるがこれはこれで困りそう
        print u"ＡＢ３".isalpha() # False
        #isalnum:英数字のみの場合にTrue
        print "abc123".isalnum()  # True
        print "abc_123".isalnum() # False
        print u"１２３".isalnum() # True 
        print u"ＡＢＣ".isalnum() # True 同上
        #isdigit:数字のみでTrue
        print "abc123".isdigit() # False 
        print "123456".isdigit() # True
        print "1234.6".isdigit() # False
        print u"１２３".isdigit() # True
        print u"ＡＢ３".isdigit() # False
        #islower:小文字のみでTrue
        print "abcedf".islower()  # True
        print "abcEDF".islower()  # False
        print "abc_df".islower()  # False
        print u"ａｂｃ".islower() # True
        print u"っょぃ".islower() # False ぅゎょぅι゛ょっょぃには反応しない
        #isupper():大文字だけならTrue
        """このパターン飽きたンゴ"""
        #isspace:空白文字だけならTrue
        print "".isspace()          # False 空文字はFalse
        print " ".isspace()         # True 半角スペース
        print "\t".isspace()        # True タブもスペース扱い
        print u"　".isspace()       # True 全角スペースもTrueになってしまう
        print " _   ".isspace()     # False
        print u" 　\t 　".isspace() # True 組み合わせ
        #istitle:タイトルケースならTrue
        """タイトルケースってなんだよ！
        タイトルケース:単語の頭だけが大文字
        たぶん要らん"""
        print "This Is A Pen".istitle()   # True
        print "THIS IS A PEN".istitle()   # False
        print "This is a pen".istitle()   # False
        print u"あぁぁぁ".istitle()       # False

    #文字列結合
    def strings_join():
        print "■文字列結合"
        #+を使って単純に結合する
        print "shibuya" + "roppongi"                              # shibuyaroppongi
        #カンマで羅列する
        print "shibuya","roppongi"                                # shibuya roppongi(半角スペースが入る)
        #join:リストを文字列で結合する
        print "->".join(("shibuya","daikanyakama","nakameguro"))  # shibuya->daikanyama->nakameguro

    strings_print()    #表示系
    getlen()           #len()で文字列長さの取得
    lower_upper()      #大文字小文字の操作
    strings_shape()    #文字列整形
    strings_find()     #文字列検索等
    enc_dec()          #エンコードデコード
    strings_replace()  #文字列置換系
    strings_separate() #文字列分割
    strings_format()   #文字列書式(formatの世界)
    valid()            #バリデーション
    strings_join() #文字列結合
