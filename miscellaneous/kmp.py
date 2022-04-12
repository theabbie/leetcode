def getLPS(pat):
    l = 0

    M = len(pat)

    lps = [0] * M

    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if l != 0:
                l = lps[l-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
    return lps

print(getLPS("azbazbzaz"))
