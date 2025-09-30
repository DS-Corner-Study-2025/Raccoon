# git init 
# : git을 본격적으로 사용하기 위해 초기 세팅
# : 프로젝트 시작 전 딱 한 번만 입력하면 됨
# 정확한 프로젝트 폴더(경로)에서 입력해야 함


# git add & commit
# 코드를 저장하는 명령어
# git add 파일명 (저장할 파일 지정)
# git add . (내 프로젝트의 변경사항을 한 번에 지정하는 방법)
# git commit -m "메세지 작성" (실제 저장)


# git status 
# 저장 여부를 확인하는 명령어


# git log
# 저장 내역을 확인하는 명령어


# git reset --hard<커밋id>
# 과거의 기록으로 돌아가는 명령어
# 커밋id는 git log 명령어로 확인 가능


# git revert <커밋id>
# 새로운 커밋 생성


# git stash
# 코드를 임시로 저장
# git stash list 
# 임시 저장 리스트 
# git stash apply <stash@뒤 숫자>
# 임시 저장되었던 코드 다시 불러옴
# -m " " : 메세지를 남길 수 있음



# 깃허브 온라인 저장소(git repository) 만들기
# 저장소 메인에 있는 "...or push an existing repository from the command line" (두 번째 칸) 옆에 있는 복사 버튼 누르고
# git에 붙여놓기 후 실행하면 파일 업로드 됨

# 이후부터는...

# 1. 코드 수정
# 2. 저장 (add & commit)
# 3. 업로드 (git push origin 브랜치명(main)) 
# git branch -M main 으로 현재 브랜치명(master)을 main으로 바꿀 수 있다
# 첫 업로드 할 때 git push -u orirgin main 이라고 하면 나중에 git push만 입력해도 git push origin main과 같은 역할을 함



# git branch 브랜치 이름
# 브랜치(복사본) 생성
# 이후 git branch를 입력하면 브랜치 생성 여부 확인 가능 (* 초록색으로 브랜치 이름)

# git switch 브랜치 이름
# 브랜치 이동 명령어

# git switch -c 브랜치 이름
# 브랜치 한 번에 생성 및 이동
# 복사본이 아닌 원본은 브랜치 이름이 main임

# github에 브랜치 업로드
# github로 이동
# Compare & pull request 클릭
# 최종 브랜치 <- 기능 브랜치
# 그 밑에 Pull request 메세지
# 메세지 작성 후 Create pull request 클릭
# Merge pull requ3est 클릭
# confirm merge 클릭
# 그럼 브랜치와 메인이 합쳐짐

# git에서 합친 것을 코드에 반영하려면
# git pull origin 브랜치명(main)

# 만약 경고문이 뜬다면?
# git config pull.rebase false 명령어 입력
# git push origin main 입력

#

