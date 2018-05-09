

# １行ずつ読み込み１行ずつ出力するパターン
def pattern_1():
    # ファイルをオープンする
    test_data = open("test_data.txt", "r", encoding="utf_8")

    # 一行ずつ読み込んで表示する
    for line in test_data:
        print(line, end="")

    # ファイルをクローズする
    test_data.close()


# 全て読み込み１行ごとにリストデータにしてから出力するパターン
def pattern_2():
    # ファイルをオープンする
    test_data = open("test_data.txt", "r", encoding="utf_8")

    # 行ごとにすべて読み込んでリストデータにする
    lines = test_data.readlines()

    # 一行ずつ表示する
    for line in lines:
        print(line, end="")

    # ファイルをクローズする
    test_data.close()


# 全て読み込み全てのデータを一度に出力するパターン
def pattern_3():
    # ファイルをオープンする
    test_data = open("test_data.txt", "r", encoding="utf_8")

    # すべての内容を読み込む
    contents = test_data.read()

    # すべての内容を表示する
    print(contents, end="")

    # ファイルをクローズする
    test_data.close()


# プログラムのエントリポイント
if __name__ == "__main__":

    print("Pattern 1")
    # パターン１を実行
    pattern_1()

    print("-------------------")
    print()

    print("Pattern 2")
    # パターン２を実行
    pattern_2()

    print("-------------------")
    print()

    print("Pattern 3")
    # パターン３を実行
    pattern_3()


