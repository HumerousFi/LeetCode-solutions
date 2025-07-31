class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime_count = 2
        composite_count = 1
        for i in range(4, n+1):
            for f in range(2, i-1):
                if i % f == 0:
                    composite_count += 1
                    break
        prime_count = n - composite_count
        print(prime_count, composite_count)
        prime_fact = 1
        for i in range(1, prime_count + 1):
            prime_fact *= i
        composite_fact = 1
        for i in range(1, composite_count + 1):
            composite_fact *= i
        # print(prime_fact, composite_fact)
        return (prime_fact*composite_fact)%(10**9+7)