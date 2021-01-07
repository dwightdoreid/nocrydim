#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader
import os, shutil

content = "All the base"

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)
env.trim_blocks = True
env.lstrip_blocks = True
env.rstrip_blocks = True

cwd = os.getcwd()

try:
    os.mkdir("site")
except:
    print("directory already exists")

os.chdir("site")

try:
    os.mkdir("images")
except:
    print("directory already exists")

os.chdir(cwd)

image_files=[
    "test_site/images/logo.jpg",
    "test_site/images/info_pic1.jpg",
    "test_site/images/info_pic2.jpg",
    "test_site/images/prod1.jpg",
    "test_site/images/prod2.jpg",
    "test_site/images/prod3.jpg"
]

for file in image_files:
    shutil.copy(file,"site/images")

# shutil.copyfile("test_site/images/logo.jpg", "site/images/logo.jpg")

template = env.get_template("index.html")

output = template.render(
content=content,
logo='"images/logo.jpg"',
biz_name="Super Calls",
info_pic1='"images/info_pic1.jpg"',
info_pic2='"images/info_pic2.jpg"',
prod1='"images/prod1.jpg"',
prod2='"images/prod2.jpg"',
prod3='"images/prod3.jpg"'
)


f = open("site/index.html", "w")
f.write(output)
f.close()

print(output)