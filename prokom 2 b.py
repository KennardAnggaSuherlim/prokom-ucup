# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:25:06 2026

@author: HP
"""

N = 10 ; i = 1 ; jumlahtinggi=0 ; banyakdata = 0

for i in range(N):
    Tinggi = int(input("berapa tinggi kamu?")) 
    jumlahtinggi= jumlahtinggi + Tinggi
    banyakdata= banyakdata + 1
    print ("jumlah tinggi:", jumlahtinggi)
    print ("===================================")

RataTinggi = jumlahtinggi / banyakdata

print ("rata rata tinggi:", RataTinggi)