from collections import Counter, defaultdict


def repeatLimitedString(s: str, repeatLimit: int) -> str:

    dic = [[char, num] for char, num in sorted(Counter(s).items(), key=lambda x: x[0], reverse=True)]
    print(dic)

    l, r = 0, 1
    res = ""
    while l < len(dic):
        char = dic[l][0]
        num = dic[l][1]
        if num <= repeatLimit:
            res += char*num
            r += 1
            l += 1
            continue

        else:
            res += char*repeatLimit
            dic[l][1] = dic[l][1] - repeatLimit
            if r < len(dic):
                res += dic[r][0]
                dic[r][1] = dic[r][1] - 1
            else:
                break

        if r < len(dic) and dic[r][1] == 0:
            dic.pop(r)

    return res


s = "xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt"
repeatLimit = 1
print(repeatLimitedString(s, repeatLimit))
