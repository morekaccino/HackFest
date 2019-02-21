from requests_html import HTML
from requests_html import HTMLSession
from logic.models import *
import os

def inserting():
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
            # print("in")
            if "/MATH" in title:
                course_links.append(link)
                crude_data = title.split()
                faculty = crude_data[0].split('/')[0]
                code = crude_data[0].split('/')[1] + ' ' + crude_data[1]
                credit = crude_data[2]
                name = " ".join(crude_data[3:len(crude_data)])
                data = {
                    "name": name,
                    "nickname": code,
                    "code": code.replace(" ",''),
                    "faculty": faculty,
                    "credit": (credit),
                    "lang": ""
                }
                print(data)
                faculty = Faculty.objects.get(name=data["faculty"])
                new_course = Course(name=data["name"],
                                    code=data["code"],
                                    nickname=data["nickname"],
                                    faculty=faculty,
                                    credit=int(float(data["credit"])),
                                    )
                new_course.save()

        except Exception as E:
            print(str(E))
