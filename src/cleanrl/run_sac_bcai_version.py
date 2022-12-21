import argparse

from src.cleanrl.sac_bcai_version import sac_main


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sac_main(parser)
