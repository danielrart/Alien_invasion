def strings_construction(a, b):
    if 3 <= len(a) <= 9 and 3 <= len(b) <= 50:
        symbol_list = []
        for sym in list(a):
            symbol_list.append(b.count(sym)/a.count(sym))
        return int( min(symbol_list))
    else:
        return 0


result = strings_construction("abb", "abcbcbaabcbcba")
print(result)
