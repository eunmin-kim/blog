import json
from datetime import date as cur_date
from os import close
def add_post_blog_list(makefile,file_name):
    file_name_dict =  {
        "name": file_name,
        "download_url": makefile
    }

    new_data = []
    try:
        with open("./data/local_blogList.json","r",encoding="utf-8") as f:
            original = json.load(f)
            original.append(file_name_dict)
        with open("./data/local_blogList.json","w",encoding="utf-8") as w:
            json.dump(original,w,ensure_ascii=False)
    except (FileNotFoundError,json.JSONDecodeError):
        return []


def add_blog_post(file_path: str, /, *, file_name):
    """
    file_path: str
    file_name: str
    /blog에 .md나 .ipynb 파일을 추가한다.
    """
    make_file = file_path+file_name
    print(file_name)
    try:
        with open(make_file,"w",encoding='utf-8') as w_file:
            md_content = """
            
            """
            w_file.write(md_content)
    except Exception as e:
        print(e)
    print("작업 완료")
    add_post_blog_list(make_file,file_name)

def get_user_inputs() -> tuple[str, str, str, str, str]:
    today = cur_date.today().strftime("%Y%m%d")
    date = input(f"날짜: 오늘 날짜는 {today} : ").strip()
    title = input("제목: ").strip()
    tag = input("태그: ").strip()
    thumbnail = input("썸네일 주소 (없을 경우 default.png): ").strip()
    description = input("간단 상세 설명: ").strip()
    return date, title, tag, thumbnail, description


def build_filename(date: str, title: str, tag: str, thumbnail: str, description: str, extension: str) -> str:
    return f"[{date}]_[{title}]_[{tag}]_[{thumbnail}]_[{description}]_[].{extension}"


def start():
    file_type = input(".md 파일 일 경우 'md', .ipynb 파일 일 경우 'ip' 입력: ").strip()
    if file_type == "md":
        print(".md 파일을 선택하셨습니다.")
        inputs = get_user_inputs()
        filename = build_filename(*inputs, extension="md")
        print("생성된 파일명:", filename)
    elif file_type == "ip":
        print(".ipynb 파일을 선택하셨습니다.")
        inputs = get_user_inputs()
        filename = build_filename(*inputs, extension="ipynb")
        print("생성된 파일명:", filename)
    else:
        print("입력된 파일 유형이 올바르지 않습니다.")
        exit()

    add_blog_post("./blog/",file_name=filename)


if __name__ == '__main__':
    start()
"""
[날짜]_[제목]_[태그]_[썸네일]_[설명]_[].md
[20250302]_[Object-Oriented with Python3]_[Python3]_[oop-thumbnail.png]_[파이썬은 정말 재미있습니다.]_[].md
"""
