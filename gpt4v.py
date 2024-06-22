from openai import OpenAI
import streamlit as st 
import requests

#open api key 값 세팅 
client = OpenAI(
    api_key = 'api 키 입력하세요'
)

#주어진 이미지 주소로부터 gpt4v의 설명을 얻는 함수 \
def describe(image_url):
    response = client.chat.completions.create(
        model = 'gpt-4-vision-preview',
        messages= [
            {'role' : 'user', 
             'content' : [
                {'type' : 'text', 'text' : '이 이미지에 대해서 알려줘'},
                {'type' : 'image_url', 'image_url' : image_url},
                ], 
            },
        ],
        max_tokens=1024,    
    )
    return response.choices[0].message.content


#웹 사이트 상단에 노출된 웹사이트 제목 
st.title('AI 도슨트: 이미지를 설명해 드려요.')

#st.text_area() >> 사용자 입력을 받는 큰 텍스트 칸을 만들어줌 
#height >> 이 텍스트 칸의 높이

input_url = st.text_area("여기에 이미지 주소를 입력해주세요!", height=30) 

#st.button()을 클릭하면 >> st.button()값이 True로 변경됨 
# >> if문이 실행됨 

if st.button('해설'):
    #st.text_area()의 값이 존재하면 input_url값이 True 되면서 if문 실행 
    if input_url:
        try:
            #st.image() >> 기본적으로 이미지 주소로부터 이미지를 웹사이트 화면에 생성 
            st.image(input_url, width=300)
            
            #describe()함수 >> gpt4v출력 결과 반환
            result = describe(input_url)
            
            #st.success() >> 텍스트를 웹사이트 화면에 출력 >> 초록색 
            st.success(result)
        except:
            st.error("요청 오류가 발생했어요.")
    else:
        st.warning('텍스트를 입력하세요')
        #st.warning >> 화면상으로 노란색 배경을 출력함
            
