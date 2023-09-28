#!/usr/bin/env python3

"""
Generates a set of NSRC stars for an artificial catalogue
    within one degree of the central sky position

RA: Central right ascension, float, decimal degrees
Dec: Central declination
NSRC: Number of stars to generate

Output: Two arrays, one of right ascensions and the other of declination
"""
import math
import random
import argparse
import logging

# Configure logging
logging.basicConfig(format="%(name)s:%(levelname)s %(message)s", level=logging.DEBUG)
log = logging.getLogger("<sky_sim>")

# Use the logger
#log.debug('This is a debug message')
#log.info('This is an info message')
#log.warning('This is a warning message')
#log.error('This is an error message')
#log.critical('This is a critical message')

NSRC = 1_000_000

def skysim_parser():
    """
    Configure the argparse for skysim

    Returns:
        parser: argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest = 'ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest = 'dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help="Destination for the output catalog")
    return parser

def generate_positions():
    """
    Generates positions of stars from Andromeda by taking
        Andromeda's position and converting to decimal degrees
    Parameters:
        Input the RA and Dec from Wikipedia
    Returns:
        RA: float, Andromeda's RA in degrees
        Dec: float, Andromeda's Dec in degrees
    """
    # From wikipedia
    andromeda_ra = '00:42:44.3'
    andromeda_dec = '41:16:09'
    log.debug("Fetching reference coordinates")

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
        ras, decs = clip_to_radius(ras, decs, ref_ra=ra, ref_dec=dec, radius=1)
    return ras, decs

def clip_to_radius(ras, decs, ref_ra, ref_dec, radius):
    ra_out = []
    dec_out = []
    for i in range(len(ras)):
        # Checks if RA and Dec falls inside the circle
        if (ras[i] - ref_ra) ** 2 + (decs[i] - ref_dec) ** 2 < radius ** 2:
            ra_out.append(ras[i])
            dec_out.append(decs[i])
    return ra_out, dec_out

def save_position_to_file(ras, decs):
    # ras, decs = make_stars(ra, dec, nsrc=NSRC)
    # Write these to a csv file for use by my other program
    with open('catalog.csv', 'w', encoding='utf8') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)
        print("Wrote catalogue.csv")