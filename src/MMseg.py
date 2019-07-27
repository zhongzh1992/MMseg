# -*-coding=utf-8-*-
import src.TrieTree as TrieTree


class Chunk:
    length = 0
    aveLen = 0
    variance = 0.0
    sumDegree = 0.0
    num = 0
    words = []


class MMseg(object):
    """
        正向最大匹配法  分词
    """

    def __init__(self, dic_path):
        self.dictionary = set()
        self.maximum = 0
        with open(dic_path, 'r', encoding='utf8') as f:
            for line in f:
                word, freq = line.split(' ')
                if not word:
                    continue
                self.dictionary.add(word)
                if len(word) > self.maximum:
                    self.maximum = len(word)

    def cut(self, text):
        return self.RMM(text)

    def MM(self, text):
        result = []
        index = 0
        while index < len(text):
            word = None
            for size in range(self.maximum, 0, -1):
                if len(text) - index < size:
                    continue
                piece = text[index:(index + size)]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index += size
                    break
            if word is None:
                result.append(text[index])
                index += 1
        return result

    def RMM(self, text):
        result = []
        index = len(text)
        while index > 0:
            word = None
            for size in range(self.maximum, 0, -1):
                if index - size < 0:
                    continue
                piece = text[index - size:index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break
            if word is None:
                result.append(text[index])
                index -= 1
        return result[::-1]


def main():
    # text = "南京市长江大桥"
    text = "自然语言处理挺有意思"
    tokenizer = MMseg('../data/defaultDictionary.txt')
    print(tokenizer.cut(text))


if __name__ == "__main__":
    main()
