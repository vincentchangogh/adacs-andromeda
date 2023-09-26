#! /usr/bin/env python
"""
Simulate a catalog of stars from the Andromeda galaxy.
"""

# Imports
import math
import random
import matplotlib.pyplot as plt

NSRC = 1_000


def generate_positions():
    # From wikipedia
    andromeda_ra = '00:40:44.3'
    andromeda_dec = '41:15:09'

    # Convert to decimal degrees
    degrees, minutes, seconds = andromeda_dec.split(':')
    dec = int(degrees) + int(minutes) / 60 + float(seconds) / 3600

    hours, minutes, seconds = andromeda_ra.split(':')
    ra = 15 * (int(hours) + int(minutes) / 60 + float(seconds) / 3600)
    ra = ra / math.cos(dec * math.pi / 180)

    return ra, dec


def make_stars(ra, dec, nsrc=NSRC):
    # Make 1000 stars within 1 degree of Andromeda
    ras = []
    decs = []
    for i in range(nsrc):
        ras.append(ra + random.uniform(-1, 1))
        decs.append(dec + random.uniform(-1, 1))
    return ras, decs

# def clip_to_radius():

def save_position_to_file():
    # Write these to a csv file for use by my other program
    with open('catalog.csv', 'w', encoding='utf8') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)
    print("Wrote catalogue.csv")


if __name__ == "__main__":
    central_ra, central_dec = generate_positions()
    ras, decs = make_stars(central_ra, central_dec)
    save_position_to_file()

# Plot and save a figure
plt.scatter(ras, decs)
plt.title("Proof of Plot: Andromeda Location in RA/DEC Degrees")
plt.xlabel("RA (deg)")
plt.ylabel("DEC (deg)")
plt.savefig("proofofplot.png")
plt.show()
