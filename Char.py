class Char:
    def __init__(self, char, sound, meaning, explain):
        self.char = char
        self.sound = sound
        self.meaning = meaning
        self.explain = explain

    def getExplainLimitLine(self, limit=19):
        lines = int(len(self.explain) / limit)
        result = ""
        if lines <= 1:
            result = self.explain
        else:
            for i in range(lines):
                if i == 0:
                    result += self.explain[0:limit-1]
                    result += '\n'
                else:
                    result += self.explain[i:(limit-1)*i]
                    result += '\n'
        return result
