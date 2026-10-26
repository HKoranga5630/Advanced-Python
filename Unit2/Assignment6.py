# Optimal Selection of Items Using 0/1 Knapsack
# Bottom-Up and Top-Down Approaches

# Bottom-Up Approach (Tabulation)
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Top-Down Approach (Memoization)
def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    memo = {}

    def solve(i, remaining_capacity):
        if i == n or remaining_capacity == 0:
            return 0

        if (i, remaining_capacity) in memo:
            return memo[(i, remaining_capacity)]

        # Option 1: Do not select the current item
        result = solve(i + 1, remaining_capacity)

        # Option 2: Select the current item if it fits
        if weights[i] <= remaining_capacity:
            result = max(
                result,
                values[i] + solve(
                    i + 1,
                    remaining_capacity - weights[i]
                )
            )

        memo[(i, remaining_capacity)] = result
        return result

    return solve(0, capacity)


# Main Program
n = int(input("Enter the number of items: "))

weights = []
values = []

for i in range(n):
    print(f"\nItem {i + 1}")
    weight = int(input("Enter weight: "))
    value = int(input("Enter value: "))

    weights.append(weight)
    values.append(value)

capacity = int(input("\nEnter maximum weight capacity: "))

if n < 0 or capacity < 0 or any(w <= 0 for w in weights):
    print("Invalid input! Use non-negative item count and capacity,")
    print("and positive weights.")
else:
    bottom_up_result = knapsack_bottom_up(weights, values, capacity)
    top_down_result = knapsack_top_down(weights, values, capacity)

    print("\nMaximum value using Bottom-Up:", bottom_up_result)
    print("Maximum value using Top-Down:", top_down_result)