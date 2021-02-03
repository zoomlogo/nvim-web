import neovim
import webbrowser

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.command('GoogleSearch', nargs=1)
    def search(self, args):
        url = 'https://google.com/search?q='

        # replace special chars
        url += args[0].replace(' ', '+')
        url += args[0].replace('!', '%21')
        url += args[0].replace('"', '%22')
        url += args[0].replace('#', '%23')
        url += args[0].replace('$', '%24')
        url += args[0].replace('%', '%25')
        url += args[0].replace('&', '%26')
        url += args[0].replace('\'', '%27')
        url += args[0].replace('*', '%2A')
        url += args[0].replace('+', '%2B')
        url += args[0].replace(',', '%2C')
        url += args[0].replace('-', '%2D')
        url += args[0].replace('.', '%2E')
        url += args[0].replace('/', '%2F')
        url += args[0].replace(':', '%3A')
        url += args[0].replace(';', '%3B')
        url += args[0].replace('<', '%3C')
        url += args[0].replace('>', '%3E')
        url += args[0].replace('=', '%3D')
        url += args[0].replace('?', '%3F')
        url += args[0].replace('@', '%40')
        url += args[0].replace('|', '%7C')
        url += args[0].replace('\\', '%5C')
        url += args[0].replace('`', '%60')
        url += args[0].replace('^', '%5E')
        url += args[0].replace('~', '%7E')
        url += args[0].replace('_', '%5F')

        # open the page
        webbrowser.open_new(url)

