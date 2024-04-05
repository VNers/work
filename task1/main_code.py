import os
import shelve


class Link:
    """Methods for work with links"""
    def __init__(self, filename):
        self.filename = filename
        self.links = self.load_links()

    def save_links(self):
        with shelve.open(self.filename) as db:
            db["links"] = self.links

    def load_links(self):
        with shelve.open(self.filename) as db:
            return db.get("links", {})

    def link_exists(self):
        return os.path.exists(self.filename)

    def shorten_link(self, start_link, short_link):
        self.links[short_link] = start_link
        self.save_links()
        print(f"The link is shortened: {short_link}")

    def expand_link(self, short_link):
        expand_link = self.links.get(short_link)
        if expand_link:
            print(f"Starting link is: {expand_link}")
        else:
            print("Link is not found! Try again!")