#!/usr/bin/env python
# coding: utf-8
"""Script to generate telescope layouts."""

from telescope import TelescopeLayout


def main():
    """."""
    tel = TelescopeLayout(name='test')
    # value of array centre from SKA-TEL-SKO-0000422 rev 2 (2016-05-31)
    tel.lon_deg = 116.7644482
    tel.lat_deg = -26.82472208

    outer_radius = 6400 + 90
    # tel.add_ska1_v5(r_min=None, r_max=outer_radius)
    print(tel.num_stations)
    tel.plot_layout()


if __name__ == '__main__':
    main()
