# -*-coding=utf-8-*-


class TrieNode:
    data = {}  # 数据
    occurances = 0  # 词频
    is_word = False  # 是否一个完整单词


class Trie:
    root = {}
    end = -1

    def __init__(self, ):
        """
        初始化根节点.
        """
        self.root = TrieNode()

    def insert(self, word, cnt):
        """
        向字典树插入一个单词
        :param word:
        :param cnt:
        :return:
        """
        node = self.root
        for chars in word:
            child = node.data.get(chars)
            if not child:
                node.data[chars] = TrieNode()
            node = node.data[chars]
        node.is_word = True
        node.occurances = cnt

    def search(self, word):
        """
        搜索字典树中是否存在某单词
        :param word:
        :return:
        """
        node = self.root
        for chars in word:
            node = node.data.get(chars)
            if not node:
                return False
        return node.is_word  # 判断单词是否是完整的存在在trie树中

    def startsWith(self, prefix):
        """
        搜索字典树是否存在某前缀
        :param prefix:
        :return:
        """
        node = self.root
        for chars in prefix:
            node = node.data.get(chars)
            if not node:
                return False
        return True


def buildTrieTree(filePath):
    t = Trie()
    fin = open(filePath, 'r', encoding='utf-8')
    for line in fin:
        parts = line.split(' ')
        k = parts[0].strip()
        v = parts[1].strip()
        t.insert(k, v)
    fin.close()
    return t


if __name__ == "__main__":
    str = "自然语言处理挺有意思"
    dic = ["自然", "语言", "处理", "自然语言处理", "挺", "有", "意思"]
    t = Trie()
    for word in dic:
        t.insert(word, 1)
    ans = t.search("自然")
    print(ans)
    ans2 = t.startsWith("自然语言处理挺")
    print(ans2)
