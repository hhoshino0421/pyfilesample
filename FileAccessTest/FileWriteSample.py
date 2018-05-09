
# 文字列を出力するパターン
def pattern_1():

    # 出力する文字列を定義
    strtext = """今は昔、竹取の翁(おきな)といふ者有りけり。野山にまじりて、竹を取りつつ、よろづのことに使ひけり。
名をば讃岐造(さぬきのみやっこ)となむ言ひける。
その竹の中に、もと光る竹なむ一筋ありける。あやしがりて寄りて見るに、筒の中光りたり。
それを見れば、三寸ばかりなる人、いと美しうて居たり。
翁言ふやう、『われ朝ごと夕ごとに見る竹の中におはするにて知りぬ。子になり給ふべき人なめり』とて、手にうち入れて家へ持ちて来ぬ。
妻(め)の嫗(おうな）に預けて養はす。美しきことかぎりなし。
いと幼ければ籠（こ）に入れて養ふ。"""

    # 書き込みモードで開く
    fileobj = open('text_data_o_1.txt', 'w', encoding="utf_8")

    # 引数の文字列をファイルに書き込む
    fileobj.write(strtext)

    # ファイルを閉じる
    fileobj.close()

# シーケンスオブジェクトを出力するパターン
def pattern_2():
    strtexts = list()
    strtexts = []

    # 出力するシーケンスを定義
    # strtexts = {'01:法專寺前', '02:八幡前', '03:変電所前', '04:警察署前', '05:上連雀８丁目', '06:市役所前', '07:農協前', '08:新川'}

    strtexts.append('01:法專寺前')
    strtexts.append('02:八幡前')
    strtexts.append('03:変電所前')
    strtexts.append('04:警察署前')
    strtexts.append('05:上連雀８丁目')
    strtexts.append('06:市役所前')
    strtexts.append('07:農協前')
    strtexts.append('08:新川')

    # デバッグ用
    # for line in strtexts:
    #    print(line)

    # 書き込みモードで開く
    fileobj = open('text_data_o_2.txt', 'w', encoding="utf_8")

    # 引数のシーケンスをファイルに書き込む
    fileobj.writelines(strtexts)

    # ファイルを閉じる
    fileobj.close()


# プログラムのエントリポイント
if __name__ == "__main__":

    # パターン１を実行
    print("pattern_1")
    pattern_1()
    print("--------------------------")

    # パターン２を実行
    print("pattern_2")
    pattern_2()
    print("--------------------------")