from numpy.core.fromnumeric import repeat
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd


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

    a = st.number_input('a를 입력하시오') 
    b = st.number_input('b를 입력하시오')
    c = st.number_input('c를 입력하시오') 
    st.number(func(a,b,c))


if __name__ == '__main__':
    main()   