def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0  
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    
    i = 0  
    j = 0  
    positions = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:  
            positions.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions

if __name__ == "__main__":
    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")

    positions = kmp_search(text, pattern)

    if positions:
        print(f"The pattern '{pattern}' occurs at positions: {', '.join(map(str, positions))}")
    else:
        print(f"The pattern '{pattern}' was not found in the text.")
