#!/usr/bin/env python
# coding: utf-8
"""Script to generate telescope layouts."""

from layout import Layout


def main():
    """."""
    layout = Layout(seed=None, num_trials=1, trail_timeout=10.0)

    # layout.x, layout.y, info = layout.rand_uniform_2d(
    #     n=256, r_max=35.0, min_sep=0.5, timeout=10.0)
    # print(info)
    # layout.apply_poly_mask(6, 35, 360//6, pad_radius=-20, invert=True)
    # layout.plot(plot_radius=35)

    layout.uniform_cluster(num_points=256, min_sep=3.4, r_max=38.0, r_min=0)
    layout.plot2(ant_radius=1.5, plot_radius=38.0, plot_radii=[38.0])

if __name__ == '__main__':
    main()
