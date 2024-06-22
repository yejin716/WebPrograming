import os 
import streamlit as st
from openai import OpenAI
import openai 

client = OpenAI(
    api_key = "api key 입력하세요"
)

st.title("OpenAI's Text to Audio Response")

#이미지 가져오기 
st.image("https://wikidocs.net/images/page/215361/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%84%B1%EC%9A%B0.jpg", width=200)

#인공지능 성우 선택박스 생성
options = ["alloy", "echo", "onyx", "nova","shimmer"]
selected_option = st.selectbox("성우를 선택해 주세요: ", options)

#인공지능 성우에게 명령 프롬프트 전달
default_text = '오늘의 생활 꿀팁을 알아볼께요.'
user_prompt = st.text_area('인공지능 성우가 읽을 스크립트를 입력해 주세요', 
                           value=default_text, height=200)

#버튼 생성 >> True(1) >> if문 실행

if st.button("Generate Audio"):
#TEXT >> VOICE 생성
    audio_response = client.audio.speech.create(
        model = 'tts-1',
        voice = selected_option,
        input = user_prompt
    )
    
    #vocie >> mp3파일로 저장 
    audio_content = audio_response.content
    
    with open('temp_mulcam_audio.mp3', 'wb') as audio_file:
        audio_file.write(audio_content)
        
    #mp3 파일 재생 
    st.audio("temp_mulcam_audio.mp3", format='audio/mp3')