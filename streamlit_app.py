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
    ["1학년", "2학년", "3학년", "4학년", "5학년", "6학년"]
)

question = st.text_area("궁금한 걸 적어줘!", placeholder="예: 무게와 질량은 뭐가 달라요?")

if st.button("AI에게 물어보기 🎈"):
    if question.strip() == "":
        st.warning("질문을 입력해줘 😊")
    else:
        with st.spinner("생각 중이에요... 🤔"):
            prompt = f"""
            너는 초등학교 {grade} 학생의 AI 학습 도우미야.
            학생이 {subject} 과목에 대한 질문을 하면,
            초등학생 눈높이에 맞게, 친절하고 재미있게 설명해줘.
            예시나 비유를 함께 사용해도 좋아.
            
            질문: {question}
            """

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": "너는 따뜻하고 친절한 초등학생 학습 도우미야."},
                          {"role": "user", "content": prompt}]
            )

            answer = response.choices[0].message.content
            st.success("🪄 AI의 대답:")
            st.write(answer)

# --- 학습 팁 ---
st.divider()
st.subheader("📚 오늘의 공부 꿀팁")
st.info("공부할 때는 궁금한 걸 바로바로 물어보면 좋아요! AI 친구가 함께 도와줄게요 💬")
