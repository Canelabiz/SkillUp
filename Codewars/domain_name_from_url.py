# [Extract the domain name from a URL](https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python)


def domain_name(url):
    return url.rsplit(".")


print(domain_name("http://google.com"), "google")
print(domain_name("http://google.co.jp"), "google")
print(domain_name("www.xakep.ru"), "xakep")
print(domain_name("https://youtube.com"), "youtube")