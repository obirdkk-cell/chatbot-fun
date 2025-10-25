import streamlit as st
from openai import OpenAI

# --- API 키 설정 ---
# st.secrets["OPENAI_API_KEY"]를 사용하는 방식 권장
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- 기본 설정 ---
st.set_page_config(page_title="초등 AI 학습 도우미", page_icon="🧠")

st.title("🧠 초등학생 AI 학습 도우미")
st.write("안녕! 나는 너의 **AI 공부 친구**야 😊 궁금한 게 있으면 편하게 물어봐!")

# --- 사용자 입력 ---
subject = st.selectbox(
    "어떤 과목을 도와줄까?", 
    ["국어", "수학", "영어", "과학", "사회", "기타"]
)

grade = st.selectbox(
    "너는 몇 학년이니?",
    ["1학년", "2학년",]()
