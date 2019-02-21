from requests_html import HTML
from requests_html import HTMLSession
from logic.models import *
import os


def prerequisite():
    print("start")
    workpath = os.path.dirname(os.path.abspath(__file__))  # Returns the Path your .py file is in
    stream = open(os.path.join(workpath, 'html_source.txt'), 'r')

    # stream = open('html_source.txt', 'r')
    stream.seek(0)
    source_code = stream.read()
    stream.close()

    html = HTML(html=source_code)
    broken_links = html.absolute_links
    working_links = []
    for i in broken_links:
        i = i.replace("example.org", "w2prod.sis.yorku.ca")
        if "w2prod.sis.yorku.ca" in i:
            working_links.append(i)

    course_links = []
    for link in working_links:
        session = HTMLSession()
        r = session.get(link)
        try:
            # print(r.html)
            title = str(r.html.find(selector='p.heading')[0].text)
            full_body = str(r.html.text)
            # print(full_body)
            if "/MATH" in title:
                course_links.append(link)
                crude_data = title.split()
                faculty = crude_data[0].split('/')[0]
                code = crude_data[0].split('/')[1] + ' ' + crude_data[1]
                credit = crude_data[2]
                name = " ".join(crude_data[3:len(crude_data)])
                about = full_body.split("Language of Instruction:")[0].split("Course Description:")[1].replace("\n",
                                                                                                               " ").strip()
                lang = "En"
                # if 'English' in about:
                #     lang = "En"
                # else:
                #     lang = "Fr"
                print(about)
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
                course = Course(name=data["name"],
                                code=data["code"],
                                nickname=data["nickname"],
                                faculty=faculty,
                                credit=int(float(data["credit"])),
                                about=data["about"],
                                lang=data["lang"])
                course.about = data["about"]
                course.lang = data["lang"]
                course.save()


        except Exception as E:
            print(str(E))
