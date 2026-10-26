# Find the Longest Common Subsequence using Dynamic Programming

def longest_common_subsequence(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Create a DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the longest common subsequence
    lcs = []
    i = m
    j = n

    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()

    return "".join(lcs), dp[m][n]


# Main Program
sequence1 = input("Enter the first sequence: ")
sequence2 = input("Enter the second sequence: ")

subsequence, length = longest_common_subsequence(sequence1, sequence2)

print("Longest Common Subsequence:", subsequence)
print("Length of LCS:", length)