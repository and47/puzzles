class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = []
        self.hist.append(homepage)
        self.pos = 1

    def visit(self, url: str) -> None:
        self.hist = self.hist[:self.pos]
        self.hist.append(url)
        self.pos += 1

    def back(self, steps: int) -> str:
        if (self.pos > steps):
            self.pos -= steps
            return(self.hist[self.pos - 1])
        else:
            self.pos = 1
            return(self.hist[0])
        

    def forward(self, steps: int) -> str:
        if (len(self.hist) - self.pos >= steps):
            self.pos += steps
            return(self.hist[self.pos - 1])
        else:
            self.pos = len(self.hist)
            return(self.hist[len(self.hist) - 1])
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)