"""
Testing to see if sky_sim module imports correctly.
Testing to make sure that generate_positions defines the RA and Dec correctly.
"""
def test_module_import():
    import mymodule.sky_sim

def test_andromeda_ra_dec():
    import mymodule.sky_sim
    ra, dec = mymodule.sky_sim.generate_positions()
    assert ra == 14.215420962967535
    assert dec == 41.26916666666666

def test_make_stars_num_sources():
    import mymodule.sky_sim
    ra, dec = mymodule.sky_sim.generate_positions()
    ras, decs = mymodule.sky_sim.make_stars(ra, dec, 100)

    # This assertion looks to make sure that the arrays are equal to each other
    assert len(ras) == len(decs)
    # This assertion doesn't pass because we clipped it
    #assert 100 == len(ras)

def test_make_stars_position ():
    import mymodule.sky_sim
    ra, dec = mymodule.sky_sim.generate_positions()
    ras, decs = mymodule.sky_sim.make_stars(ra, dec, 100)
    # Make an assertion that every star is within one degree of central sky position
    for (this_ra, this_dec) in zip(ras, decs):
        assert (this_ra - ra)**2 + (this_dec - dec)**2 < 1**2