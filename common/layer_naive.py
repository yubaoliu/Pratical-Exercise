class MulLayer:
    #インスタンス変数であるｘとｙの初期化を行いますが、これらは、順伝播の入力値を保持するために用います
    def __init__(self):
        self.x = None
        self.y = None
    
    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x*y
        return out
    # 上流から伝わってきた微分に対して、順伝播の”ひっくり返した値”を乗算して下流に流れします.
    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x
        return dx, dy


class AddLayer():
    def __init__(self):
        pass
    def forward(self, x, y):
        out = x + y
        return out
    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy

