import fitz
from gtts import gTTS
import re

# PDF 파일 열기
while True:
    pdf_path = input("pdf 파일 경로를 입력하세요 (ex: C:\\Users\\user\\Downloads\\example.pdf): ")

    try:
        pdf_document = fitz.open(pdf_path)
        print("pdf 파일이 성공적으로 열렸습니다")
        text = ""
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text += page.get_text()

        pdf_document.close()
        break
    except Exception as e:
        print(f"에러가 발생했습니다: {e}")
        print("경로를 다시 입력 해주세요 \n")

# 출력 오디오파일 이름만들기
paths = pdf_path.split("\\")
output_audio_path = f'{paths[-1][:-4]}.mp3'

# 특수문자를 제거
text = re.sub(r'[^\w\s]', '', text)

# 텍스트를 음성으로 변환
try:
    tts = gTTS(text=text, lang='ko')  # 한국어로 설정
    print("잠시만 기다려주세요~")
    tts.save(output_audio_path)
    print(f"음성 파일이 {output_audio_path}로 저장되었습니다.")
except Exception as e:
    print(f"음성 변환 중 오류가 발생했습니다: {e}")

