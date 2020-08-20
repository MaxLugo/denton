import denton
import numpy as np

'''
Taken from: https://www.imf.org/external/pubs/ft/qna/pdf/2017/chapter6.pdf
Table: Example 6.2
'''
help(denton.proportional_method)

I = np.array([99.4,99.6,100.1,100.9,101.7,102.2,102.9,
     103.8,104.9,106.3,107.3,107.8,107.9,
     107.5,107.2,107.5])
A = np.array([1000, 1040, 1060.8, 1064.9])

#the average of every 4 in the data annual data
B = denton.proportional_method(I, A)

#to replicate the table then divide by 4
B_imf = denton.proportional_method(I, A)/4

print(B_imf)















