# 터미널 할 일 목록

Python 표준 라이브러리만 사용하는 간단한 CLI 할 일 관리 프로그램입니다.

## 실행

Python 3.9 이상에서 저장소 폴더로 이동한 뒤 실행하세요.

```bash
python main.py
```

할 일 데이터는 실행 폴더의 `tasks.json`에 저장됩니다. 이 파일은 개인 데이터이므로 Git에서 제외됩니다.

## GitHub에 올리기

1. GitHub에서 **New repository**를 눌러 저장소를 만듭니다. README와 `.gitignore`는 추가하지 않아도 됩니다.
2. 아래 명령을 프로젝트 폴더에서 실행하고 `<사용자명>`과 `<저장소명>`을 바꿉니다.

```bash
git init
git add .
git commit -m "Initial commit: CLI todo app"
git branch -M main
git remote add origin https://github.com/<사용자명>/<저장소명>.git
git push -u origin main
```

Git을 처음 쓰는 컴퓨터라면 이름과 이메일을 먼저 설정하세요.

```bash
git config --global user.name "GitHub 표시 이름"
git config --global user.email "GitHub 이메일 주소"
```

다음 변경부터는 아래 세 명령으로 커밋하고 푸시하면 됩니다.

```bash
git add .
git commit -m "변경 내용 요약"
git push
```
