class Sentence:
    @staticmethod
    def classify(sentence):
        sentence = sentence.strip()
        if sentence=="":
            return 'blank'
        if sentence.find(":-")!=-1:
            return 'rule'
        return 'fact'

    @staticmethod
    def next(input):
        line = 0
        next_line = input[line].strip()
        if next_line:
            while not next_line.endswith('.'):
                line += 1
                next_line += input[line].strip()
        return next_line, input[line + 1:]