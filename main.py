import streamlit as st
import time

st.title('Streamlit入門')

st.write('ブログレスバー')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.01)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに表示')
if button:
    right_column.write('右を表示しました！')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ内容を書く')
expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ内容を書く')
# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 5, 10)

# 'あなたのしゅみは',text
# 'コンディション:' ,condition

# if st.checkbox('Show Image'):
#     img = Image.open('mockup.jpg')
#     st.image(img,caption = 'nirasakuseijpg' ,use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50]+ [35.69,139.70],
#     columns=['lat', 'lon']
# )
# df
# st.table(df.style.highlight_max(axis=0))
# st.map(df)
