from urlparse import urlparse


def join_url_to_directory(url, directory):
    ends_with = url.endswith('/')
    starts_with = directory.endswith('/')

    if ends_with and starts_with:
        return ''.join((url, directory[1:]))

    if ((ends_with and not starts_with) or
        (not ends_with and starts_with)):
        return ''.join((url, directory))

    if not ends_with and not starts_with:
        return ''.join((url, '/', directory))

    raise Exception('Unhandled case')


class URL:
    """Represents an url with information extracted so that it's easly
    accessible"""

    def __init__(self, url):
        self.url = url
        parsed = urlparse(url)
        self.scheme = parsed.scheme
        self.path = parsed.path
        self.params = parsed.params
        self.query = parsed.query
        self.fragment = parsed.fragment

        if '@' in parsed.netloc:
            login_password, self.domain = parsed.netloc.split('@')
            self.login, self.password = login_password.split(':')
        else:
            self.domain = parsed.netloc
            self.login = self.password = None

        if ':' in self.domain:
            self.domain, self.port = self.domain.split(':')
        else:
            self.port = None