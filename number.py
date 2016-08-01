#!/usr/bin/python
#-*-coding: utf-8 -*-
import os
"""
ファイルに列番号をつけるソースコードです.
1回目は番号をつけたいファイル名を入力する.
2回目は番号をつけたものを出力するファイルを入力する.
入力ファイル名では、他のディレクトリにあるものを使う時は絶対パスで入力してください.
例:~/Downloads/sample.txtのように指定してください.
"""
def number(tekist):
	fp=open(tekist)
	#ファイルを読み込む
	a=fp.readlines()
	#行数を抜き取る
	length=len(a)
	c=[]
	#段落づけ
	for i in range(length):
		b=a[i]
		c.append(str(i+1)+' '+b)
	fp.close()
	print(c) 
	return(c , length)
	
#ファイルに書き込む関数
def output(list_number,length,afterfile):
	fp=open(afterfile,'w')
	for j in range(length):
		fp.write(list_number[j])
	fp.close()
	
	return 0
#変換する関数
def changetiruda(before):
	d=[]
	char=''
	dis=os.path.dirname(os.path.abspath(__file__))
	#ルートディレクトリを探し出す。
	for i in range(10):
		dis=os.path.dirname(os.path.abspath(dis))
		d.append(dis)
		#'/'ならば抜ける
		if d[i]== '/':
			break
	#ルートディレクトリをrootに格納
	root=d[-3]
	change=list(before)
	#~であった時に行う操作
	if change[0]=='~':
		#~を消す
		change.remove("~")
		for z in range(len(change)):
			char+=change[z]
		#絶対パスを取得する。
		chars=root+char
		return chars
	else:
		return before
		
#main関数	
if __name__ == '__main__':
	beforefile=input('元のファイルを入力してください:')
	beforefiles=changetiruda(beforefile)
	afterfile=input('出力ファイルを入力してください:')
	#番号付け関数を呼び出す
	list_number,lengths=number(beforefiles)
	#ファイルに出力する
	jud=output(list_number,lengths,afterfile)

	if(jud==0):
			print('成功しました')
	else:
			print('失敗しました')
