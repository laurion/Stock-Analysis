#price['0']/price['-4']>1.05
result[code][name] = stock[date][code].max(5) > stock.index(-4).close * 1.05
