# `rank_roi`

The CIAO [`roi`](https://cxc.cfa.harvard.edu/ciao/ahelp/roi.html) tool 
is used to convert say a source list into a stack of region
files, aka Region Of Interest (not _return on investment_).

The `roi` tool has a lot of options to control things like the 
background region, including the detector edges via the field
of view file, etc.  

When regions overlap it has several `group` options.

- `group=group` creates 1 region file per bundle of sources that overlap.
- `group=individual` creates 1 region file per source and ignores any
overlaps.
- `group=exclude` creates 1 region file per source.  Any overlapping
sources are excluded from each other.

## `group=exclude`

The `exclude` setting is the most common usages of `roi`. 


