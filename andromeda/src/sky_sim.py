#! /usr/bin/env python
"""
Simulate a catalog of stars from the Andromeda galaxy.
"""

# Imports
import math
import random
import matplotlib.pyplot as plt

NSRC = 1_000_000
# From wikipedia
andromeda_ra = '00:42:44.3'
andromeda_dec = '41:16:09'

def generate_positions():
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
        # Apply our filter
        # ras, decs = clip_to_radius(ras, decs)
    return ras, decs

def clip_to_radius(ras, decs, ref_ra, ref_dec, radius):
    """
    Crop an input list of positions so that they lie within radius of
    a reference position

    Parameters:
    ----------
    ras,decs : list(float)
        The ra and dec in degrees of the data points
    ref_ra, ref_dec: float
        The reference location
    radius: float
        The radius in degrees

    Returns:
    -------
    ras, decs : list
        A list of ra and dec coordinates that pass our filter.
    """
    ra_out = []
    dec_out = []
    for i in range(len(ras)):
        # Checks if RA and Dec falls inside the circle
        if (ras[i] - ref_ra) ** 2 + (decs[i] - ref_dec) ** 2 < radius ** 2:
            ra_out.append(ras[i])
            dec_out.append(decs[i])
    return ra_out, dec_out

def save_position_to_file():
    # Write these to a csv file for use by other program
    with open('catalog.csv', 'w', encoding='utf8') as f:
        print("id,ra,dec", file=f)
        for i in range(len(ras)):
            print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)
    print("Wrote catalogue.csv")

if __name__ == "__main__":
    central_ra, central_dec = generate_positions()
    ras, decs = make_stars(central_ra, central_dec)
    ras, decs = clip_to_radius(ras, decs, central_ra, central_dec, 1)
    save_position_to_file()

# Plot and save a figure
plt.scatter(ras, decs)
plt.title("Proof of Plot: Andromeda Location in RA/DEC Degrees")
plt.xlabel("RA (deg)")
plt.ylabel("DEC (deg)")
plt.savefig("proofofplot.png")
#plt.show()