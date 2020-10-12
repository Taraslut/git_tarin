from my_pack import sub_mod1, sub_mod2
from sys import version_info
import requests

print(version_info)
text = requests.get('http://google.com.ua')
print(text)
print(text.text)
print(sub_mod1.hello('sdf'))
print(sub_mod2.good_foo())
