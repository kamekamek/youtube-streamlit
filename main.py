import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'


left_column, right_column = st.columns(2)

button = left_column.button('右カラムを表示')

if button:
    right_column.write('こんにちは')


expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')

expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# text = st.sidebar.text_input(
#     'あなたの趣味を教えてください'
# )
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味:', text
# 'コンディション：', condition



# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11)),
#     index=2
# )

# 'あなたの好きな数字は、', option, 'です'

# if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='Kame', use_column_width=True)

# df = pd.DataFrame({
#     '1列目':[1, 2, 3, 4],
#     '2列目':[10, 20, 30, 40]
# })

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70 ],
#     columns=['lat', 'lon']
# )

# st.map(df)

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)


# st.write(df, width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0)) #動的な表
# st.table(df.style.highlight_max(axis=0))# 静的な表


# """
# # マークダウンもできる
# ```python
# import streamlit
# ```
# """

