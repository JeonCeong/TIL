from numpy.core.fromnumeric import repeat
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd


yes_list = ["yes", "Yes", "YES", "yeah", "Yeah", "YEAH", "Y", "y"]

def func(a,b,c): #2차 방정식 계산 함수(본 함수만 사용)
    D=b**2-4*a*c
    if D>0:
        x1=round((-b-D**0.5)/2*a)
        x2=round((-b+D**0.5)/2*a)
        print("x =",x1,",",x2)
    elif D==0:
        x=round(-b/2*a)
        print("중근입니다")
        print("x =",x)
    else:
        print("허근입니다")
        
        
def main(): #main 함수는 예시로 제작
     file = st.sidebar.level = st.slider("레벨을 선택하세요.", 1, 5)

    while True:
        try:
            print('                                                ')
            print('------------------------------------------------')
            print('   2차 방정식의 근을 구해주는 프로그램 입니다 ')
            print('------------------------------------------------')
            print('   2차 방정식의 기본 형태 : aX^2 + bX + c = 0   ')
            print('----------------------------------------------')
            a = float(input('        a의 값을 입력하십시오 : '))
            b = float(input('        b의 값을 입력하십시오 : '))
            c = float(input('        c의 값을 입력하십시오 : '))
            print('----------------------------------------------')
            func(a,b,c)
            
            print('----------------------------------------------')
            ans = input("다시 진행하시겠습니까? [y/n] >>")
            if ans in yes_list:
                continue
                print('----------------------------------------------')
                print('                                              ')
            else:
                break
                
        except:
            print('----------------------------------------------')
            print('*******************ERROR!!********************')
            print('----------------------------------------------')
            print("          숫자를 입력하시기 바랍니다.         ")
            


if __name__ == '__main__':
    main()   