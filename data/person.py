import streamlit as st
import pandas as pd
import numpy as np

st.markdown("#❄️การวิเคราะห์รายบุคคล❄️")
st.sidebar.markdown("# รายบุคคล❄️")
st.sidebar.title("การออกแบบสรรถนะการเรียนรู้ด้านAI 5 ด้าน")
st.sidebar.button("ออกแบบ")
st.sidebar.radio("ด้านที่ 1",["สูง","กลาง","ต่ำ"])
st.sidebar.radio("ด้านที่ 2",["สูง","กลาง","ต่ำ"])
st.sidebar.radio("ด้านที่ 3",["สูง","กลาง","ต่ำ"])
st.sidebar.radio("ด้านที่ 4",["สูง","กลาง","ต่ำ"])
st.sidebar.radio("ด้านที่ 5",["สูง","กลาง","ต่ำ"])

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.header("รายงานสถิติของข้อมูล")
st.write(df.describe())

st.header("ตัวอย่างของข้อมูล")
st.write(df.head(20))

#st.table(df)
st.header("การจินตทัศน์ข้อมูล")

st.bar_chart(df)