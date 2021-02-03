import neovim
import webbrowser

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.command('GoogleSearch', nargs=1)
    def search(self):
        self.vim.command(f'echo "hello"')

