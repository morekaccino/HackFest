from requests_html import HTML
from requests_html import HTMLSession
from logic.models import *
import os


def prerequisite():
    print("start")
    session = HTMLSession()
    r = session.get("https://calendars.students.yorku.ca/2016-2017/computer-science")
    try:
        r.html.text.find()
        # print(r.html)
        title = str(r.html.find(selector='p.heading')[0].text)
        full_body = str(r.html.text)
        # print(full_body)
        if "/EECS" in title:
            course_links.append(link)
            crude_data = title.split()
            faculty = crude_data[0].split('/')[0]
            code = crude_data[0].split('/')[1] + ' ' + crude_data[1]
            credit = crude_data[2]
            name = " ".join(crude_data[3:len(crude_data)])
            about = full_body.split("Language of Instruction:")[0].split("Course Description:")[1].replace("\n"," ").strip()
            lang = "En"
            data = {
                "name": name,
                "code": code,
                "nickname": code,
                "faculty": faculty,
                "credit": (credit),
                "lang": lang,
                "about": about,
            }
            # print(data)
            faculty = Faculty.objects.get(name=data["faculty"])
            course = Course.objects.get(name=data["name"],
                                    code=data["code"],
                                    nickname=data["nickname"],
                                    faculty=faculty,
                                    credit=int(float(data["credit"])),
                                    )
            course.about = data["about"]
            course.lang = data["lang"]
            course.save()


    except Exception as E:
        print(str(E))
