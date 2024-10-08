from bs4 import BeautifulSoup as Bsoup

def failed(expression):
    return not expression

def makePost(tag: Bsoup):
    post = tag.find_all("div", recursive=False, limit=2)[1].find("div").find("div").find("div").find("div").find_all("div", recusrive=False, class_="post-text") 
    return "<hr>".join(map(str, post))


def hyperlink(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)
