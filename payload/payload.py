import settings

trail_start = 2
org_pri = float(settings.public_auth.ticker(tpair=settings.pair)['last'])
print(org_pri)
neg = []
pos = []


def trail_neg():
    if org_pri - float(settings.public_auth.ticker(tpair="BTCUSD")['last']) > trail_start:
        trail = float(settings.public_auth.ticker(tpair="BTCUSD")['last']) + trail_start
        if len(neg) == 0:
            neg.append(trail)
        elif neg[-1] > trail and neg[-1] != trail:
            neg.append(trail)

    print('======================= Sell trail stop ========================')
    print()
    print(neg)
    print()
    print('================================================================')


def trail_pos():
    if float(settings.public_auth.ticker(tpair="BTCUSD")['last']) - org_pri > trail_start:
        trail = float(settings.public_auth.ticker(tpair="BTCUSD")['last']) - trail_start
        if len(pos) == 0:
            pos.append(trail)
        elif pos[-1] < trail and pos[-1] != trail:
            pos.append(trail)

    print('======================= Buy trail stop =========================')
    print()
    print(pos)
    print()
    print('================================================================')


def logic():
    print(trail_neg())
    print(trail_pos())
