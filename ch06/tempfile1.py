import tempfile

# 무작위의 임시 파일을 생성한다.

filename = tempfile.mkdtemp()
tempfile.mkdtemp()
print(filename)