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
        args = args[0].replace(' ', '+')
        args = args.replace('!', '%21')
        args = args.replace('"', '%22')
        args = args.replace('#', '%23')
        args = args.replace('$', '%24')
        args = args.replace('%', '%25')
        args = args.replace('&', '%26')
        args = args.replace('\'', '%27')
        args = args.replace('*', '%2A')
        args = args.replace('+', '%2B')
        args = args.replace(',', '%2C')
        args = args.replace('-', '%2D')
        args = args.replace('.', '%2E')
        args = args.replace('/', '%2F')
        args = args.replace(':', '%3A')
        args = args.replace(';', '%3B')
        args = args.replace('<', '%3C')
        args = args.replace('>', '%3E')
        args = args.replace('=', '%3D')
        args = args.replace('?', '%3F')
        args = args.replace('@', '%40')
        args = args.replace('|', '%7C')
        args = args.replace('\\', '%5C')
        args = args.replace('`', '%60')
        args = args.replace('^', '%5E')
        args = args.replace('~', '%7E')
        args = args.replace('_', '%5F')
        url += args

        # open the page
        webbrowser.open_new(url)

