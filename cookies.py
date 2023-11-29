import http.cookiejar
import urllib
import ssl



def obtainCookies():
    url='https://wikipedia.com'
    cookie_jar=http.cookiejar.CookieJar()
    url_opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    context = ssl.create_default_context(cafile="/Users/mac/test_code/venv/lib/python3.12/site-packages/certifi/cacert.pem")

    url_opener.open(url)
    for cookie in cookie_jar:
        print(cookie.name, cookie.value)
obtainCookies()
