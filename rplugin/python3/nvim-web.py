import neovim
import webbrowser

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.command('GoogleSearch')
    def doItPython(self, args):
        self.vim.command(f'echo "hello from {args}"')

