# 파일 입출력 1 - 쓰기

# mode = w새로생성쓰기 a추가쓰기 r읽기
f = open(file='C:/STUDY/StudyPython/temp.txt', mode='w', encoding='utf-8')

f.write('안녕하세요.\n')
f.write('저는 성명건입니다.\n')
f.write('한국사람이죠.\n')

f.close() ##필수
print('파일 생성완료')
