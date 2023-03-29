import streamlit as st
import pandas as pd
import numpy as np

html_21="""
<div style="background-color:#575EB5;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
 <center><h3>การวิเคราะห์รายชั้นปี</h3></center>
</div>
"""
st.image('./pic/ban23.png')
st.markdown(html_21,unsafe_allow_html=True)
st.markdown("xxxxx")
st.markdown("")
st.sidebar.markdown("# วิเคราะห์รายชั้นปี ")

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

html_22="""
<div style="background-color:#575EB5;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
<h5>รายงานสถิติของข้อมูล </h5>
</div>
"""
st.markdown(html_22,unsafe_allow_html=True)
if st.button("แสดงข้อมูลสถิติ"):
   st.write(df.describe())
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

html_23="""
<div style="background-color:#575EB5;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
<h5>ตัวอย่างของข้อมูล </h5>
</div>
"""
st.markdown(html_23,unsafe_allow_html=True)
if st.button("แสดงข้อมูล"):
   st.write(df.head(20))
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

#st.table(df)
html_24="""
<div style="background-color:#575EB5;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
<h5>การจินตทัศน์ข้อมูล </h5>
</div>
"""
st.markdown(html_24,unsafe_allow_html=True)
if st.button("แสดงการจินตทัศน์ข้อมูล"):
   st.write(df.head(20))
   st.area_chart(df)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

st.subheader("การออกแบบสรรถนะการเรียนรู้ด้านAI 5 ด้าน")

options1 = st.multiselect(
     'กรุณาเลือกออกแบบการเรียนรู้ด้านที่1',
     ['สูง', 'กลาง', 'ต่ำ'])
st.write('คุณเลือกดังนี้', options1)

options2 = st.multiselect(
     'กรุณาเลือกออกแบบการเรียนรู้ด้านที่2',
     ['สูง', 'กลาง', 'ต่ำ'])
st.write('คุณเลือกดังนี้', options2)

options3 = st.multiselect(
     'กรุณาเลือกออกแบบการเรียนรู้ด้านที่3',
     ['สูง', 'กลาง', 'ต่ำ'])
st.write('คุณเลือกดังนี้', options3)

options4 = st.multiselect(
     'กรุณาเลือกออกแบบการเรียนรู้ด้านที่4',
     ['สูง', 'กลาง', 'ต่ำ'])
st.write('คุณเลือกดังนี้', options4)

options5 = st.multiselect(
     'กรุณาเลือกออกแบบการเรียนรู้ด้านที่5',
     ['สูง', 'กลาง', 'ต่ำ'])
st.write('คุณเลือกดังนี้', options5)

if st.button("ออกแบบ"):
    html_25="""
<div style="background-color:coral;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>🎉คุณได้ทำการออกแบบ 🎉</h4>
        1.ด้านที่ 1 สูง <br>
        2.ด้านที่ 2 กลาง <br>
        3.ด้านที่ 3 กลาง <br>
        4.ด้านที่ 4 สูง <br>
        5.ด้านที่ 5 สูง <br>
</center>
</div>
"""
    st.markdown(html_25,unsafe_allow_html=True)
    st.image('./pic/04.png')
    st.button("ยังไม่ออกแบบ")
else:
    st.write("ไม่ออกแบบ")