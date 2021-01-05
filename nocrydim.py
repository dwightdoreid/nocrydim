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

shutil.copyfile("test_site/images/logo.jpg", "site/images/logo.jpg")

template = env.get_template("index.html")
output = template.render(
content=content,
logo='"images/logo.jpg"',
biz_name="Super Calls"
)
f = open("site/index.html", "w")
f.write(output)
f.close()

print(output)