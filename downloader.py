# downloader.py
#
# A utility class for downloading data.

# import logging     # TODO...
from urllib import request
from urllib.request import Request, ProxyHandler, HTTPBasicAuthHandler, HTTPHandler, urlopen, HTTPError, URLError


class Downloader:
    def __init__(self, proxy):
        super(Downloader, self).__init__()
        self.proxy = proxy

    def download(self, url):
        """ Downloads content from the given URL.  A boolean is returned indicating success or failure. """
        try:
            if self.proxy is not None and self.proxy.usesProxy():
                proxy_handler = ProxyHandler({'http': 'http://{}:{}@{}:{}'.format(self.proxy.proxyUser, self.proxy.proxyPassword, self.proxy.proxyUrl, self.proxy.proxyPort),
                                              'https': 'https://{}:{}@{}:{}'.format(self.proxy.proxyUser, self.proxy.proxyPassword, self.proxy.proxyUrl, self.proxy.proxyPort)})
                proxy_auth_handler = HTTPBasicAuthHandler()
                opener = request.build_opener(proxy_handler, proxy_auth_handler, HTTPHandler)

                # This installs it globally, so it can be used with urlopen().
                request.install_opener(opener)

            self.request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            self.data = urlopen(self.request).read()
            return True

        except URLError as e:
            if hasattr(e, 'reason'):
                errMsg = "Could not connect to server when fetching: {}: {}".format(url, e.reason)
            elif hasattr(e, 'code'):
                errMsg = "Could not fulfill request when fetching: {}: {}".format(url, e.code)
            else:
                errMsg = "Unknown URL Exception."

            print(errMsg)
            #logging.error(errMsg)

            self.data = None
            return False

        except ValueError as e:
            errMsg = "ValueError exception when fetching image: {}: {}".format(url, e)
            print(errMsg)
            #logging.error(errMsg)
            self.data = None
            return False

        except Exception as inst:
            errMsg = "Exception when fetching {}: {}".format(url, inst)
            print(errMsg)
            #logging.error(errMsg)
            self.data = None
            return False

    def getData(self):
        return self.data

    def getDataAsString(self):
        if self.data is not None:
            return self.data.decode('utf-8')
        else:
            return ""
