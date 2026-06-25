class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = []
        self.stack.append(homepage)
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.forward_stack = []

    def back(self, steps: int) -> str:
        while steps > 0:
            if self.stack:
                self.forward_stack.append(self.stack.pop())
            steps -= 1
        if self.stack:
            return self.stack[-1] 
        else:
            # edge case: back removes all, then you visit. the visited pg must come AFTER the last remaining pg (which got removed by back)
            self.stack.append(self.forward_stack.pop()) 
            return self.stack[-1]

    def forward(self, steps: int) -> str:
        if not self.forward_stack:
            return self.stack[-1]

        for i in range(steps):
            if self.forward_stack:
                self.stack.append(self.forward_stack.pop())

        return self.stack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)