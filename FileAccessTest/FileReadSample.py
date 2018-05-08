
def pattern_1():
    # ファイルをオープンする
    test_data = open("test_data.txt", "r")

    # 一行ずつ読み込んで表示する
    for line in test_data:
        print(line)

    # ファイルをクローズする
    test_data.close()


def pattern_2():
    # ファイルをオープンする
    test_data = open("test_data.txt", "r")

    # 行ごとにすべて読み込んでリストデータにする
    lines = test_data.readlines()

    # 一行ずつ表示する
    for line in lines:
        print(line)

    # ファイルをクローズする
    test_data.close()

def pattern_3():
    # ファイルをオープンする
    test_data = open("test_data.txt", "r")

    # すべての内容を読み込む
    contents = test_data.read()

    # すべての内容を表示する
    print(contents)


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


