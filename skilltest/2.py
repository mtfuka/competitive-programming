import csv
with open('in.tsv', mode='r', newline='', encoding='utf-8') as f: #読み込み用としてTSVファイルを開く
   tsv_reader = csv.reader(f, delimiter='\t') #データの読み込み
   data = [row for row in tsv_reader] #二次元リストとして取得

for i in range(len(data)-1): #最終の2行の比較までなので、iは(dataのサイズ-1)まで
    for j in range(i+1,len(data)): #i列目とi列目以降の全ての列を比較する
        if(data[i][0]==data[j][0]):
            data[i][1]+=":"+data[j][1]
            data[j][0]="@" #同じキーを持つ列をマーク

out = [data[i] for i in range(len(data)) if not data[i][0]=="@"] #キーが@になっている列以外を抽出して新しいリストを作成

#ファイルで出力する場合
with open('out.tsv', mode='w', newline='', encoding='utf-8') as fo: #書き込み用としてTSVファイルを開く
    tsv_writer = csv.writer(fo, delimiter='\t') #データの書き込み
    tsv_writer.writerows(out)

#標準出力で出力する場合
#for i in out:
#    print(*i, sep='\t')

#python 2.py 実行するためのコマンド
