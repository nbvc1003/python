import zipfile
import tarfile

# Zip으로 압축
filelist = ["E:/nbvc/python/01.파이썬 개요.pdf"]
with zipfile.ZipFile('py.zip','w', compression=zipfile.ZIP_BZIP2) as mz:
    for temp in filelist:
        mz.write(temp)

zipfile.ZipFile('py.zip').extractall()

# tar로 압축
filelist2 = ["E:/nbvc/python/02.파이썬의 자료형.pdf"]
with tarfile.open('tarz.tar.gz', 'w:gz') as mytar:
    for temp in filelist2:
        mytar.add(temp)

tarfile.open('tarz.tar.gz').extractall()

