import streamlit as st
import openai

# 사이드바에서 API 키 입력 받기
st.sidebar.title("API 설정")
api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if api_key:
    # OpenAI 클라이언트 초기화
    openai.api_key = api_key

    # Streamlit 페이지 제목 설정
    st.title("환경 보호 4컷 만화 생성기")

    # 사용자 입력 받기
    prompt = st.text_input("과학적 개념을 입력하세요. 예: 재활용, 대기 오염 방지 등")

    # 버튼을 클릭했을 때 이미지 생성
    if st.button("이미지 생성"):
        if prompt:
            # 입력된 과학적 개념을 환경 보호하는 4컷 만화 형식으로 만드는 프롬프트 생성
            for i in range(1, 5):
                modified_prompt = f"A cartoon illustration of {prompt} in scene {i} that shows how it helps to protect the environment"

                # OpenAI API를 사용하여 이미지 생성
                try:
                    response = openai.Image.create_variation(
                        image=None,  # 이미지 파일은 제공하지 않음
                        prompt=modified_prompt,
                        n=1,
                        size="512x512"
                    )

                    # 생성된 이미지 URL 가져오기
                    image_url = response['data'][0]['url']

                    # 이미지 출력
                    st.image(image_url, caption=f"Scene {i}: {modified_prompt}")
                except Exception as e:
                    st.error(f"이미지를 생성하는 중 오류가 발생했습니다: {e}")

            # 그림에 대한 설명 생성
            explanation_prompt = f"Explain in detail how {prompt} contributes to protecting the environment."
            try:
                explanation_response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=explanation_prompt,
                    max_tokens=150
                )

                # 설명 출력
                explanation_text = explanation_response.choices[0].text.strip()
                st.subheader("그림에 대한 설명")
                st.write(explanation_text)
            except Exception as e:
                st.error(f"설명을 생성하는 중 오류가 발생했습니다: {e}")
        else:
            st.warning("과학적 개념을 입력하세요.")
else:
    st.warning("API 키를 사이드바에 입력하세요.")