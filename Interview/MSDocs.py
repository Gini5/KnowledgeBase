# <p><a>link</a> b <div>c</div></p>

# open_tag a
# text link
# close_tag </a>
# <p> --> <a> --> link
# <p> --> <a> --> link
# --> b
# --> <div> --> c

# html_token {
# }

# html_node {
# }
# html_token[] --> html_node { }

class Token:
    def __init__(self, typ, content):
        self.type = typ
        self.content = content

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def token2node(tokens):
    root = Node(0)
    s_node = [root]
    for token in tokens:
        if token.type == 'open_tag':
            new = Node(token.content)
            s_node[-1].children.append(new)
            s_node.append(new)
        elif token.type == 'text':
            s_node[-1].children.append(Node(token.content))
        else: 
            if not s_node or s_node[-1].val != token.content:
                continue
            else:
                s_node.pop()
    return s_node[0]


token2node([Token('open_tag','a'),
            Token('text','b'),
            Token('close_tag', 'c'),
            Token('close_tag','a')])