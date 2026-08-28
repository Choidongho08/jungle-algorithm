"""
def is_palindrome(s):
    new_s = ""
    for a in s:
        if a.isalnum():
            a = a.lower()
            new_s += a

    n = len(new_s)
    
    if n % 2 != 0:
        for i in range(n-1):
            if new_s[i] != new_s[-i-1]:
                return False
    else:
        for i in range(n):
            if new_s[i] != new_s[-i]:
                return False

    return True
"""

# 개선 with ai
def is_palindrome(s):
    new_s = ''.join(a.lower() for a in s if a.isalnum())

    n = len(new_s)

    for i in range(n // 2):
        if new_s[i] != new_s[-i-1]:
            return False

    return True


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f"입력: \"{test1}\"")
    print(f"회문 여부: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f"입력: \"{test2}\"")
    print(f"회문 여부: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f"입력: \"{test3}\"")
    print(f"회문 여부: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "Madam"
    result4 = is_palindrome(test4)
    print(f"입력: \"{test4}\"")
    print(f"회문 여부: {result4}")

