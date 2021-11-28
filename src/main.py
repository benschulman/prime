from prime.constants import MED_BOUND
from prime.constants import STAR_WITNESSES_XLARGE
from prime.prime import miller_rabin_prime


def main():
    print(MED_BOUND)
    for wit in STAR_WITNESSES_XLARGE:
        prime = miller_rabin_prime(MED_BOUND, wit)
        print(f"Witness: {wit}, {prime}")


if __name__ == "__main__":
    main()
