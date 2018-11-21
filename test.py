#!/usr/bin/env python3

xml_string = ""
with open("sites.txt", "r") as sites:
    for site in sites:
        string = "<string>{0}</string>".format(site.strip())
        xml_string += string

print("3")
print(xml_string)

