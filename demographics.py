import functools
import requests

from bs4 import BeautifulSoup

def get_soup(url, method="GET", data=None):
    print(f"Fetching {url} via {method} and parameters {data}")
    if method == "GET":
        page = requests.get(url, timeout=60)
    elif method == "POST":
        page = requests.post(url, data=data, timeout=60)

    soup = BeautifulSoup(page.content, "html.parser")
    return soup



@functools.lru_cache
def extract_table(state="TX", year=1960):
    soup = get_soup('https://www.ssa.gov/cgi-bin/namesbystate.cgi', method="POST", data={"state":state,"year":year})
    #print(soup)
    caption = soup.find('caption')
    #if caption.get_text() == 'Popularity for top 100 names in Texas for births in 1960':
    table = caption.find_parent('table')
    #print(table)


    rows = table.find_all('tr')
    output_data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if len(cols) == 5:
            row_num, male_name, male_pop, female_name, female_pop = cols
            struct = {
                "male_name": male_name,
                "male_population": male_pop,
                "female_name": female_name,
                "female_population": female_pop,
            }
            #print(f"{row_num} - {struct}")
            output_data.append(struct)
    return output_data

def gather_name_data(state="TX"):
    for year in range(1960, 2010):
        bits = extract_table(state, year)
        print(bits)

if __name__ == "__main__":
    gather_name_data()
