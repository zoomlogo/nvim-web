import neovim
import webbrowser

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.command('GoogleSearch', nargs=1)
    def search(self, args):
        url = 'https://google.com/search?q='
        url += args[0].replace(' ', '+')
        webbrowser.open_new(url, 2)

