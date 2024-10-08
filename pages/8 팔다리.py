import streamlit as st
from openai import OpenAI

# 사이드바에서 API 키 입력 받기
st.sidebar.title("API 설정")
api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if api_key:
    # OpenAI 클라이언트 초기화
    client = OpenAI(api_key=api_key)

    # Streamlit 페이지 제목 설정
    st.title("환경 보호 만화 생성기")

    # 사용자 입력 받기
    prompt = st.text_input("과학적 개념을 입력하세요. 예: 재활용, 대기 오염 방지 등")

    # 버튼을 클릭했을 때 이미지 생성
    if st.button("이미지 생성"):
        # 입력된 과학적 개념을 환경 보호하는 만화 형식으로 만드는 프롬프트 생성
        modified_prompt = f"A cartoon illustration of {prompt} that shows how it helps to protect the environment"

        # OpenAI API를 사용하여 이미지 생성
        response = client.images.generate(
            model="dall-e-3",
            prompt=modified_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # 생성된 이미지 URL 가져오기
        image_url = response.data[0].url

        # 이미지 출력
        st.image(image_url, caption=f"Generated Image: {modified_prompt}")

        # 그림에 대한 설명 생성
        explanation_prompt = f"Explain in detail how {prompt} contributes to protecting the environment."
        explanation_response = client.completions.create(
            engine="text-davinci-003",
            prompt=explanation_prompt,
            max_tokens=150
        )

        # 설명 출력
        explanation_text = explanation_response.choices[0].text.strip()
        st.subheader("그림에 대한 설명")
        st.write(explanation_text)
else:
    st.warning("API 키를 사이드바에 입력하세요.")