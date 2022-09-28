#!/usr/bin/env python3

# Inspired by https://github.com/aianta/cgi-lab

import cgi
import os
from templates import login_page, secret_page

header = ""
body = ""

def check_cookies(cookie_string):
    if cookie_string == "":
        return {}
    cookies = cookie_string.split(";")
    result = {}
    for cookie in cookies:
        split_cookie = cookie.split("=")
        result[split_cookie[0]] = split_cookie[1]
    return result

cookies = check_cookies(os.environ["HTTP_COOKIE"])

form = cgi.FieldStorage()

username = form.getfirst("username")
password = form.getfirst("password")

header += "Content-Type: text/html\r\n"

if username is not None or ("logged" in cookies and cookies["logged"] =="true"):
    body += secret_page(username,password)
    header += "Set-Cookie: logged=true; Max-Age=60\r\n"
    header += "Set-Cookie: cookie=nom"
    body += "<h1> HUsh Hush </h1>"
else:
    body += login_page()

print(header)
print()
print(body)

