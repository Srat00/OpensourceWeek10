def bm_match(txt: str, pat: str) -> int:
    pt = len(pat)
    tt = len(txt)
    if pt == 0 or tt == 0 or pt > tt:
        return []

    last_occurrence = {}
    for i in range(pt):
        last_occurrence[pat[i]] = i

    i = pt - 1
    while i < tt:
        k = pt - 1
        while k >= 0 and txt[i] == pat[k]:
            i -= 1
            k -= 1
        if k == -1:
            return i + 1
        else:
            last = last_occurrence.get(txt[i])
            i += max(pt - k, 1) if last is None else max(pt - k, 1, k - last)
    return -1

if __name__ == '__main__':
    s1 = input("텍스트 입력: ")
    s2 = input("패턴 입력: ")

    idx = bm_match(s1, s2)

    if idx == -1:
        print("텍스트 안에 패턴이 존재하지 않습니다.")
    else:
        print(f"{idx + 1}번째 문자가 일치합니다.")
