#! /usr/bin/python
# -*- encoding: utf-8 -*-
__author__= "koichi-ezato"
__date__ = "$2014/10/10"

import mojimoji

# unicodeをutf-8にエンコードする
def unicode_to_utf8(r):
	return r.encode('utf-8')

# 全角文字を全て半角文字に変換
print '----- 全角→半角変換 -----\r\n'
print 'target:アイウａｂｃ０１２\r\n'

zenAll = u'アイウａｂｃ０１２'
r = mojimoji.zen_to_han(zenAll)

print unicode_to_utf8(r)

# 全角カナ以外の全角文字を全て半角に変換
r = mojimoji.zen_to_han(zenAll, kana = False)
print unicode_to_utf8(r)

# 全角数字以外の全角文字を全て半角に変換
r = mojimoji.zen_to_han(zenAll, digit = False)
print unicode_to_utf8(r)

# 全角アスキー文字以外の全角文字を全て半角に変換
r = mojimoji.zen_to_han(zenAll, ascii = False)
print unicode_to_utf8(r)
print '\r\n----- 全角→半角変換 -----\r\n'

# 半角文字を全て全角文字に変換
print '----- 半角→全角変換 -----\r\n'
print 'target:ｱｲｳabc012\r\n'

hanAll = u'ｱｲｳabc012'

# 半角文字を全て全角文字に変換
r = mojimoji.han_to_zen(hanAll)
print unicode_to_utf8(r)

# 半角カナ以外の半角文字を全て全角に変換
r = mojimoji.han_to_zen(hanAll, kana = False)
print unicode_to_utf8(r)

# 半角数字以外の半角文字を全て全角に変換
r = mojimoji.han_to_zen(hanAll, digit = False)
print unicode_to_utf8(r)

# 半角アスキー文字以外の半角文字を全て全角に変換
r = mojimoji.han_to_zen(hanAll, ascii = False)
print unicode_to_utf8(r)
print '\r\n----- 半角→全角変換 -----\r\n'
