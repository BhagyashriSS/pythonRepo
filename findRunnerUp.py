{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 ArialMT;}
{\colortbl;\red255\green255\blue255;\red69\green85\blue94;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c34118\c40784\c44314;\cssrgb\c100000\c100000\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww21560\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \AppleTypeServices\AppleTypeServicesF65539 \cf2 \cb3 \expnd0\expndtw0\kerning0
#Given the participants' score sheet for your University Sports Day, you are required to find #the runner-up score. You are given\'a0\'a0scores. Store them in a list and find the score of the #runner-up.\
if __name__ == '__main__':\
    n = int(input())\
    arr = list(map(int, input().split()))\
    arr.sort()\
    maxVal = arr[-1]\
    while arr[-1] == maxVal:\
      arr.pop()\
    print(arr[-1])}