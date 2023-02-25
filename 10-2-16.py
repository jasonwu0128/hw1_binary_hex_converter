# -*- coding: utf-8 -*-
"""二進位與十六進位

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NEAofspSBKzI_apVJ5Z4j8C0vTyyYIUQ
"""

try: #如果下面程式發生錯誤則直接執行except
  number1 = int(input('請輸入0-255間的正整數'))
  if number1 > 255:
    print('輸入數字超過範圍，請重新輸入0-255間的正整數')
  elif number1 < 0:
    print('輸入數字為負數，請重新輸入0-255間的正整數')
  elif number1 == 0:
    print('二進位數字為0')
    print('十六進位數字為0') #如果輸入數字為零，直接顯示為0
  #if number1 < 0:
    #print('輸入數字為負數，請重新輸入0-255間的正整數')
  else:
    Q = number1
    Ans = []
    while Q >1:  #二進位制將各個餘數算出即可得
      R = Q%2 #先取得R餘數
      Q = Q//2 #算出Q商數
      Ans.append(R) #將餘數加入到答案串列中
    if Q == 1:  
      Ans.append(Q) #Q是1的話，將Q加入答案串列
    #Ans.reverse() 可以反轉串列
    a= len(Ans) #a算出串列元素個數
    answer2 = ''
    for i in range(a-1,-1,-1): #從最後一個元素到第一個，間隔為反向-1
      answer2 = answer2+str(Ans[i]) #將串列中的元素轉成字串反向加入二進位答案變數中
    print('二進位數字為'+answer2)
    number16 = 0
    answer16 = []
    dict1 = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'} #字典將大於10的數字轉成英文字母
    for k in range(0,a): #重複執行串列個數
      number16 = number16+Ans[k]*2**(k%4) #先將二進位數字個別乘以2的(k(元素編號)除以4的餘數)以得到十進位值
      #print(number16) 測試用
      if number16>=10: #若十進位值大於十必然已經算完四個位數，將其找出字典中對應的字母並加入答案串列中
        answer16.append(dict1[number16])
        number16 =0 #再將數值歸零以計算下四位數的數值
      elif k%4==3: #如果沒大於十，但是還是算完四個位數(餘數等於3)，將其加入串列並歸零數值
        answer16.append(str(number16))
        number16 =0
    if number16 !=0: #最後如果沒有算到剛好四個位數，剩下值不為零，就再將其加入串列中
      answer16.append(str(number16))
    answer16s=''
    for i in range(len(answer16)-1,-1,-1): #將串列中的元素轉成字串反向加入十六進位答案變數中
      answer16s = answer16s+str(answer16[i])
    print('十六進位數字為'+answer16s)
      
except:
  print('輸入錯誤，請重新輸入0-255間的正整數')

