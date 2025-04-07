from math import comb

def mendel(filename):
    # Read integers k, m, n from a text file
    with open(filename, "r") as f:
        line = f.readline().strip()
    k, m, n = map(int, line.split())

    # Total number of organisms
    total = k + m + n

    # Total number of ways to choose 2 organisms from the population
    total_pairs = comb(total, 2)

    # Probability calculation:
    # 1. Two homozygous dominant (DD, from k)
    # 2. One DD (k) and one Dd (m)
    # 3. One DD (k) and one dd (n)
    # 4. Two Dd (m) => 3/4 chance of dominant phenotype
    # 5. One Dd (m) and one dd (n) => 1/2 chance of dominant phenotype
    # 6. Two dd (n) => 0 chance of dominant phenotype

    prob = 0.0

    # 1. Both from k (DD,DD)
    prob += comb(k, 2) * 1.0

    # 2. One from k (DD) and one from m (Dd)
    prob += k * m * 1.0

    # 3. One from k (DD) and one from n (dd)
    prob += k * n * 1.0

    # 4. Both from m (Dd,Dd) => 3/4 chance
    prob += comb(m, 2) * 0.75

    # 5. One from m (Dd) and one from n (dd) => 1/2 chance
    prob += m * n * 0.5

    # 6. Both from n (dd,dd) => 0 chance, so we don't add anything

    # Divide by total number of pairs to get the overall probability
    prob /= total_pairs

    # Print the result
    print(prob)