class item:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight

def fraction(w,arr):
    arr.sort(key=lambda x:(x.profit/x.weight),reverse=True)
    value=0.0
    for item in arr:
        if item.weight <= w:
            w -= item.weight
            value += item.profit
        else:
            value += item.profit * w / item.weight
            break
    return value

if __name__=="__main__":
    w=80
    arr=[item(60,10), item(100,20), item(120, 30)]
    max_val = fraction(w,arr)
    print(max_val)