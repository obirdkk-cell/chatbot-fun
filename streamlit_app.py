import streamlit as st
from openai import OpenAI

# ---------------------------
# 기본 페이지 설정
# ---------------------------
st.set_page_config(page_title="연령 맞춤형 AI 학습 도우미", page_icon="🎓", layout="wide")
st.title("🎓 연령 맞춤형 AI 학습 도우미")
st.caption("사용자 연령에 따라 난이도를 조절해 설명해주는 AI 선생님 챗봇입니다.")

# ---------------------------
# API Key 입력
# ---------------------------
openai_api_key = st.text_input("🔑 OpenAI API Key를 입력하세요", type="password")
if not openai_api_key:
    st.info("계속하려면 OpenAI API Key를 입력해주세요.", icon="🗝️")
else:
    client = OpenAI(api_key=openai_api_key)

    # ---------------------------
    # 사용자 연령 선택
    # ---------------------------
    user_level = st.radio(
        "📚 학습 대상 선택:",
        ["초등학생", "중학생", "고등학생", "성인"],
        horizontal=True
    )

    # ---------------------------
    # 연령별 설명 스타일 프롬프트
    # ---------------------------
    if user_level == "초등학생":
        system_prompt = (
            "너는 초등학생에게 인공지능 개념을 재미있고 쉽게 설명하는 선생님이야. "
            "예시와 비유를 사용하고, 어린이가 이해하기 쉬운 단어로 이야기해줘."
        )
    elif user_level == "중학생":
        system_prompt = (
            "너는 중학생에게 AI 개념을 친절하게 설명하는 선생님이야. "
            "조금 더 구체적인 원리와 예시를 포함하고, 쉬운 전문용어도 사용해줘."
        )
    elif user_level == "고등학생":
        system_prompt = (
            "너는 고등학생에게 AI 기술을 체계적으로 설명하는 강사야. "
            "기본 개념과 응용 사례를 논리적으로 설명해주고, 관련 진로나 학습 방법도 함께 알려줘."
        )
    else:  # 성인
        system_prompt = (
            "너는 성인 학습자에게 AI 기술과 활용법을 실무 중심으로 설명하는 전문가야. "
            "AI 모델 구조, 활용 사례, 실습 방법 등을 단계적으로 안내해줘."
        )

    # ---------------------------
    # 세션 초기화
    # ---------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": system_prompt}]

    # 대화 새로 시작 버튼
    if st.button("🧹 대화 새로 시작하기"):
        st.session_state.messages = [{"role": "system", "content": system_prompt}]
        st.rerun()

    # ---------------------------
    # 이전 대화 표시
    # ---------------------------
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # ---------------------------
    # 사용자 입력
    # ---------------------------
    if prompt := st.chat_input(f"{user_level} 수준으로 궁금한 내용을 물어보세요!"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # ---------------------------
        # GPT 응답 생성
        # ---------------------------
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # ---------------------------
        # 응답 출력
        # ---------------------------
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
