import sys


def split_num(n, path):
    # 分割ファイル１つあたりの行数を返す関数
    split_list = []
    file_lines = sum([1 for _ in open(path)])  # ファイルの行数のカウント
    q, mod = divmod(file_lines, n)
    for i in range(n):  # 分割されたものにそれぞれ何行入るかのリストを作成 n=4ならsplit_list=[6,6,6,6]
        split_list.append(q)
    for i in range(mod):  # 余りを一つずつ配分していく
        split_list[i] += 1
    return split_list


def split(split_list, path):
    # 分割ファイル１つあたりの行数のリストを引数に分割したものを出力
    with open(path) as fi:
        for split in split_list:
            for i in range(split):
                print(fi.readline().strip())
            print("-----")

            
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('コマンドライン引数が不適切です')
        print('python q14.py [出力したい行数] [入力ファイル]')
    lis = split_num(int(sys.argv[1]), sys.argv[2])
    split(lis, sys.argv[2])
