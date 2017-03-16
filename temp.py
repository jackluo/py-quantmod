
test1 = dict(
    a = 1,
    b = 2,
    c = dict(
        la = 1,
        si = 2,
    ),)

test2 = dict(
    a = dict(
        gagaga = 10,
        gaga = 9,
        basd = dict(
            aass = 10001,
        ),
    ),
    b = 4,)

test1.update(test2)
test1

def merge_dict(d1, d2):
    d = d2.copy()
    for k, v in list(d1.items()):
        if k not in d:
            d[k] = v
        else:
            if isinstance(v, dict):
                d[k] = merge_dict(d1[k], d[k])
    return d

merge_dict(test1, test2)

z = {**test1, **test2}
z
