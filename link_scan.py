from selenium import  webdriver
import requests
import sys

def get_links(url:str):
    """Find all links on page at the given url.

           Returns:
              a list of all unique hyperlinks on the page,
              without page fragments or query parameters.
    """
    driver = webdriver.Chrome("/Users/panitanplengkham/Desktop/link-scanner/chromedriver")
    driver.get(url)
    url_list = []
    for elements in driver.find_elements_by_xpath("//a[@href]"):
        if "#" in elements.get_attribute("href"):
            continue
        elif "?" in elements.get_attribute("href"):
            continue
        else:
            if not elements.get_attribute("href") in url_list:
                url_list.append(elements.get_attribute("href"))
    return url_list

def is_valid_url(url:str):
    """
    Return True if the URL is OK, False otherwise.
    """
    try:
        response = requests.head(url)
        response.raise_for_status()
    except requests.HTTPError:
        return False
    return True

def invalid_urls(url:list):
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    bad_list = []
    for i in url:
        if not is_valid_url(i):
            bad_list.append(i)
    return bad_list


def main():
    if len(sys.argv) < 2:
        print("Usage:  python3 link_scan.py url")
    else:
        url_list = get_links(sys.argv[1])
        bad_url_list = invalid_urls(url_list)
        for i in url_list :
            print(i)
        print("Bad Links:")
        for i in bad_url_list:
            print(i)


if __name__ == '__main__':
    main()
