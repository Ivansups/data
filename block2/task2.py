def missing_number(nums: list) -> int:
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

# Сложность: O(n) по времени, O(1) по памяти