import sys


def begin_n_line(n, path):
    with open(path) as fi:
        print(''.join([fi.readline() for i in range(n)]))
            
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('コマンドライン引数が不適切です')
        print('python q14.py [出力したい行数] [入力ファイル]')
    begin_n_line(int(sys.argv[1]), sys.argv[2])
