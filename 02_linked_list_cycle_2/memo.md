# Step1
- 空間計算量`O(1)`の解法は思いつかなかったので`set`を使用したコードを作成したが、後から`O(1)`の解説を`step1.py`に再現してしまったので紛失したので、以下に再現した。
  - かなりシンプルで、これ以上の改善箇所が思いつかなかったため、step2以降では空間計算量`O(1)`の解法だけをブラッシュアップした。
```python
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes: set[ListNode] = set()
        node = head
        
        while node is not None:
          if node in visited_nodes:
            return node
          
          visited_nodes.add(node)
          node = node.next
          
        return None
```
- step1での再現コードでは、最後まで`faster`と`slower`という変数を最後までゴリ押ししてしまったが、`faster`と`slower`とが合流した後の変数名としては実態に則していないと思いながら書いた。
- 1つ目の`while`ループの条件と、そのループを抜けた後の`faster`が`tail`に到達しているかどうかを判定する箇所が（否定を除いて）全く同じで、もう少しスッキリしたコードが書けるのではないかと思った。

# Step2
- step1で感じた、１度目の合流後の変数名を変えてみた。`faster`の方は先行している位置にいるので`predecessor`、`slower`の方は逆に`successor`としてみた。
- 一つ目の`while`ループを抜けた後、`tail`に到達していたら`None`を返す処理を素直にループの下に書いてあって良いのか迷った。
  - とはいえ、これより良い書き方が思いつかなかったため、step2ではそのままにした。

# Step3
- step2とほぼ同じコード（コメントの英語だけちょっと変わった）をスラスラかけたので、一旦終了とした。

# Step4
- コードの整え方のコメント集を読み、自然な言語化を意識したコードを書く練習をした。
- 今回の処理を言語化してみると以下のようになるため、合流点を探す処理を関数として切り出すのが一番自然なのではと思った。
  - (フロイドの循環検出法を用いて)合流点を探す
    - 合流点がなければ終了
  - 合流点とヘッドを始点にしたときの合流点を探す。そこが答え。

