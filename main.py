import streamlit as st
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i)
    time.sleep(0.05)

'Done!!'
left_column,right_column = st.columns(2)
button = left_column.button('右に表示')
if button:
    right_column.write('右')

expander = st.expander('例えばこんな場合')
expander.write('詳細をここに')
