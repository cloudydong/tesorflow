import sys
import subprocess


# 필요 패키지 설치 -> 설치 불필요 시 주석 처리
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


for pk in ['pandas', 'numpy', 'matplotlib', 'tensorflow']:
    install(pk)


if __name__ == '__main__':
    # code
    print("finish")
