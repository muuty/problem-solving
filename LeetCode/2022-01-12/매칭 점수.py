import re
from collections import defaultdict

def solution(word, pages):
    word = word.lower()
    basic_scores = {}
    external_links_dict = defaultdict(list)
    external_link_counts = {}
    scores = []

    for page in pages:
        url = get_page_url(page)
        basic_score = get_basic_score(page, word)
        external_links = get_external_links(page)
        external_link_counts[url] = len(external_links)
        for link in external_links:
            external_links_dict[link].append(url)

        basic_scores[url] = basic_score

    for url in basic_scores:
        scores.append(basic_scores[url] + sum([basic_scores[link] / external_link_counts[link] for link in external_links_dict[url]]))
    return scores.index(max(scores))


def get_page_url(page):
    return re.search('<meta property="og:url" content="(\S+)"', page).group(1)



def get_basic_score(page, word):
    cnt = re.sub('[^a-zA-Z]', ' ', page).lower().split().count(word.lower())
    return cnt

def get_external_links(page):
    return re.findall('<a href="(https://[\S]*)"', page)