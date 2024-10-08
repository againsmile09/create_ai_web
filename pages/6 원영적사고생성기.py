import streamlit as st
import google.generativeai as genai

# 사이드바에서 API 키 입력 받기
st.sidebar.title("API 설정")
api_key = st.sidebar.text_input("Google Gemini API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if api_key:
    # API 키 설정
    genai.configure(api_key=api_key)

    # Streamlit 페이지 제목 설정
    st.title("원영적 사고 생성기")

    # 생성 설정
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # 모델 초기화
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # 사용자 입력 받기
    user_input = st.text_area("사고을 생성할 내용을 입력하세요", 
                              "예: 민수는 아주 힘든 하루를 보냈어요.")

    if st.button("사고 생성"):
        # 인공지능 모델을 사용하여 사고 생성
        response = model.generate_content([
            "고등학생에게 부정적인 사고를 긍정적인 사고의 말로 바꿔 얘기해주려고 합니다. 입력의 내용을 참고하여 재치있고, 희망적인 문구를 생성해주세요. 그리고 럭키비키를 꼭 포함해서 작성해줘야해. 핵심이야",
            f"input: {user_input}",
        ])

        # 결과 출력
        st.subheader("생성된 원영적 사고")
        st.write(response.text)
else:
    st.warning("API 키를 사이드바에 입력하세요.")
