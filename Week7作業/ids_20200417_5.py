# -*- coding: utf-8 -*-
"""IDS_20200417_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14mv2LNTNDriEalztvBO9ihgnI_3cS3J0
"""

id_last_digit = input("請輸入您身分證字號的尾數:")
id_last_digit = int(id_last_digit)
if id_last_digit % 2 == 1:
    ans = "星期一三五日領"
else:
    ans = "星期二四六領"
print(ans)