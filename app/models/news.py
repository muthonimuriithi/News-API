class Article:

    def __init__(self, title, author, date, description, url, url_to_image):
        self.title = title
        self.author = author
        self.date = date
        self.description = description
        self.url_to_image = url_to_image
        self.url = url


class Source:
    def __init__(self, id, name):
        self.id = id
        self.name = name
