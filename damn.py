import re
code = ""
with open("code.txt", "r") as f:
    code += f.read()

class ComplexityFinder:
    def __init__(self):
        self._counter = 0

    def findClosingBracket(self, start_index):
        stack = []
        for i, char in enumerate(code[start_index:]):
            if char == "{":
                stack.append(i + start_index)
            elif char == "}":
                if not stack:
                    return -1
                start = stack.pop()
                if not stack:
                    return i + start_index
        return -1
    
    def findFor(self, start, end):
        self.for_counter = 0
        def recursive(start_pos, end_bracket):
            next_for = code.find("for", start_pos, end_bracket)
            next_while = code.find("while", start_pos, end_bracket)
            next_bracket = code.find("{", start_pos, end_bracket)
            if (next_for != -1 or next_while != -1) and next_bracket != -1:
                self.for_counter += 1
                recursive(next_bracket+1, end_bracket)
            self.start_pos = start_pos
        recursive(start, end)
        return self.for_counter
    
    def findComplexity(self):
        self.complexity = 0
        while self._counter < len(code)-1:
            next_start = code.find("{", self._counter)
            next_end = self.findClosingBracket(next_start)
            for_counter = self.findFor(next_start+1, next_end)
            self._counter += next_end+1
            if for_counter > self.complexity:
                self.complexity = for_counter
        return self.complexity
    
complexityFinder = ComplexityFinder()
print(complexityFinder.findComplexity())