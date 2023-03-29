import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.markdown("# การวิเคราะห์รายโรงเรียน❄️")
st.sidebar.markdown("# 🎈🎈โรงเรียน❄️")

st.sidebar.title("การออกแบบสรรถนะการเรียนรู้ด้านAI 5 ด้าน")
st.sidebar.button("ออกแบบ")
st.sidebar.radio("ด้านที่ 1",["สูง","กลาง","ต่ำ"])
st.sidebar.radio("ด้านที่ 2",["สูง","กลาง","ต่ำ"])
st.sidebar.radio("ด้านที่ 3",["สูง","กลาง","ต่ำ"])
st.sidebar.radio("ด้านที่ 4",["สูง","กลาง","ต่ำ"])
st.sidebar.radio("ด้านที่ 5",["สูง","กลาง","ต่ำ"])

df = pd.DataFrame(
   np.random.randn(100, 3),
   columns=['x','y','z']
   )

st.table(df)

c = alt.Chart(df).mark_circle().encode(
   x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])

st.header("รายงานสถิติของข้อมูล")
st.write(df.describe())

st.header("ตัวอย่างของข้อมูล")
st.write(df.head(20))

#st.table(df)
st.header("การจินตทัศน์ข้อมูล")

st.altair_chart(c, use_container_width=True)