import pandas as pd
from tqdm import tqdm

from prime.prime import is_prob_prime
from prime.prime import miller_rabin_prime

# from prime.constants import MED_BOUND


def main():
    not_primes_odds = list()
    # precompute non-primes (odds):
    for i in tqdm(range(7, 50000, 2), desc="Pre-computing non-primes..."):
        if not is_prob_prime(i):
            not_primes_odds.append(i)

    # dict of liars
    liars = dict()
    # loop over a large number of value
    for i in tqdm(not_primes_odds, desc="Calculating Liars..."):
        # for every possible witness
        for wit in range(2, i):
            # check if the witness says it is prime
            mr_prime = miller_rabin_prime(i, wit)
            # if the witness says it's a prime, then it is a liar
            if mr_prime:
                # update liars dict
                if wit not in liars:
                    liars[wit] = 1
                else:
                    liars[wit] += 1

    sorted_items = sorted(
        liars.items(), key=lambda x: (x[1], -x[0]), reverse=True
    )
    df = pd.DataFrame(sorted_items, columns=["Witness", "Liar Count"])
    print(df.head())
    df.to_csv("liars.csv", index=False)


if __name__ == "__main__":
    main()
