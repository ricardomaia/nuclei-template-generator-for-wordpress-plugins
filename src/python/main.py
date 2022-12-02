__author__ = "Ricardo Maia"
__copyright__ = "Copyright 2022, Ricardo Maia"
__credits__ = ["Ricardo Maia"]
__license__ = "GPL v3"
__version__ = "0.0.3"
__email__ = "rsmaia@gmail.com"
__status__ = "Development"

"""
This is the main file of the project. It is the entry point of the application.
"""

from time import sleep
from bs4 import BeautifulSoup
import requests
import re
from markdown import markdown
from termcolor import colored, cprint

# Regex to extract the name of th plugin from the URL
regex = r"https://wordpress.org/plugins/(\w.+)/"

ranking = 1

# Top 200 Wordpress Plugins
for page_number in range(1, 11):

    html = requests.get(url=f"https://wordpress.org/plugins/browse/popular/page/{page_number}", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
        "Pragma": "no-cache",
    }).content

    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find(id="main")
    articles = results.find_all("article", class_="plugin-card")

    # Set top_tag
    top_tag = "top-100,top-200" if page_number <= 5 else "top-200"

    # Get each plugin in the page
    for article in articles:

        full_title = article.find("h3", class_="entry-title").get_text()
        regex_remove_quotes = r"[\"`]"
        subst_remove_quotes = "'"
        title = re.sub(regex_remove_quotes, subst_remove_quotes, full_title)

        link = article.find("a").get("href")
        name = re.search(regex, link).group(1)

        cprint(f"Title: {title}", "cyan")
        cprint(f"Link: {link}", "yellow")
        cprint(f"Name: {name} - Ranking: {ranking}", "green")
        print(f"Page Number: {page_number}")
        print(f"Top Tag: {top_tag}")
        print(f"http://plugins.svn.wordpress.org/{name}/trunk/readme.txt")
        ranking += 1

        sleep(0.2)

        # Get the readme.txt file from SVN
        readme = requests.get(
            url=f"http://plugins.svn.wordpress.org/{name}/trunk/readme.txt",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Host": "plugins.svn.wordpress.org",
                "Pragma": "no-cache",
                "Upgrade-Insecure-Requests": "1",
                "Referer": "http://plugins.svn.wordpress.org/{name}/trunk/"}).content

        # Extract the plugin version
        try:
            version = re.search(r"(?i)Stable.tag:\s+([\w.]+)",
                                readme.decode("utf-8")).group(1)
        except:
            version = "N/A"

        # Extract the plugin description
        try:
            description_markdown = re.search(
                r"(?i)==.Description.==\W+\n?(.*)", readme.decode("utf-8")).group(1)
            html = markdown(description_markdown)
            full_description = BeautifulSoup(html, 'html.parser').get_text()
            regex_max_length = r"(\b.{80}\b)"
            subst_max_lenght = "\\g<1>\\n    "
            description = re.sub(
                regex_max_length, subst_max_lenght, full_description, 0, re.MULTILINE)
        except:
            description = "N/A"

        print(f"Version: {version}")
        print(f"Description: {description}")

        # Write the plugin template to file
        template = f'''id: wordpress-{name}

info:
  name: "{title} Detection"
  author: ricardomaia
  severity: info
  reference:
    - https://wordpress.org/plugins/{name}/
  metadata:
    plugin_namespace: {name}
    wpscan: https://wpscan.com/plugin/{name}        
  tags: tech,wordpress,plugin,{top_tag}

requests:
  - method: GET
    redirects: true
    max-redirects: 2
    path:
      - "{{{{BaseURL}}}}/wp-content/plugins/{name}/readme.txt"
    matchers-condition: and      
    matchers:
      - type: regex
        regex:
          - '(?i)Stable.Tag'
      - type: status
        status:
          - 200
    extractors:
      - type: regex
        name: version
        part: body
        group: 1
        regex:
          - '(?i)Stable.tag:\s?([\w.]+)'
'''

        # print(template)
        template_file = open(f"/templates/wordpress-{name}.yaml", "w")
        template_file.write(template)
        template_file.close()

        print("--------------------------------------------")
        print("\n")
