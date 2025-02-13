"""
Hardcoded coordinates for board cells, could be done dynamically in the future to support custom board sizes.
And different screen sizes of course. Currently only supports 1920x1080.

Chose to use the Box namedtuple because it allows easy back and forth between the center of a cell for clicking and the whole area of a cell for detection.

For now this suffices well if all the initialization steps are done properly to ensure the sizes always match.

Values gotten from get_utils.ipynb
"""

from collections import namedtuple
Box = namedtuple("Box", ["left", "top", "width", "height"])

# easy
easy_grid = [
  [Box(left=674, top=331, width=34, height=35), Box(left=708, top=331, width=34, height=35), Box(left=743, top=331, width=34, height=35), Box(left=778, top=331, width=34, height=35), Box(left=812, top=331, width=34, height=35), Box(left=847, top=331, width=34, height=35), Box(left=882, top=331, width=34, height=35), Box(left=916, top=331, width=34, height=35), Box(left=951, top=331, width=34, height=35)],
  [Box(left=674, top=366, width=34, height=35), Box(left=708, top=366, width=34, height=35), Box(left=743, top=366, width=34, height=35), Box(left=778, top=366, width=34, height=35), Box(left=812, top=366, width=34, height=35), Box(left=847, top=366, width=34, height=35), Box(left=882, top=366, width=34, height=35), Box(left=916, top=366, width=34, height=35), Box(left=951, top=366, width=34, height=35)],
  [Box(left=674, top=401, width=34, height=35), Box(left=708, top=401, width=34, height=35), Box(left=743, top=401, width=34, height=35), Box(left=778, top=401, width=34, height=35), Box(left=812, top=401, width=34, height=35), Box(left=847, top=401, width=34, height=35), Box(left=882, top=401, width=34, height=35), Box(left=916, top=401, width=34, height=35), Box(left=951, top=401, width=34, height=35)],
  [Box(left=674, top=436, width=34, height=35), Box(left=708, top=436, width=34, height=35), Box(left=743, top=436, width=34, height=35), Box(left=778, top=436, width=34, height=35), Box(left=812, top=436, width=34, height=35), Box(left=847, top=436, width=34, height=35), Box(left=882, top=436, width=34, height=35), Box(left=916, top=436, width=34, height=35), Box(left=951, top=436, width=34, height=35)],
  [Box(left=674, top=471, width=34, height=35), Box(left=708, top=471, width=34, height=35), Box(left=743, top=471, width=34, height=35), Box(left=778, top=471, width=34, height=35), Box(left=812, top=471, width=34, height=35), Box(left=847, top=471, width=34, height=35), Box(left=882, top=471, width=34, height=35), Box(left=916, top=471, width=34, height=35), Box(left=951, top=471, width=34, height=35)],
  [Box(left=674, top=506, width=34, height=35), Box(left=708, top=506, width=34, height=35), Box(left=743, top=506, width=34, height=35), Box(left=778, top=506, width=34, height=35), Box(left=812, top=506, width=34, height=35), Box(left=847, top=506, width=34, height=35), Box(left=882, top=506, width=34, height=35), Box(left=916, top=506, width=34, height=35), Box(left=951, top=506, width=34, height=35)],
  [Box(left=674, top=541, width=34, height=35), Box(left=708, top=541, width=34, height=35), Box(left=743, top=541, width=34, height=35), Box(left=778, top=541, width=34, height=35), Box(left=812, top=541, width=34, height=35), Box(left=847, top=541, width=34, height=35), Box(left=882, top=541, width=34, height=35), Box(left=916, top=541, width=34, height=35), Box(left=951, top=541, width=34, height=35)],
  [Box(left=674, top=576, width=34, height=35), Box(left=708, top=576, width=34, height=35), Box(left=743, top=576, width=34, height=35), Box(left=778, top=576, width=34, height=35), Box(left=812, top=576, width=34, height=35), Box(left=847, top=576, width=34, height=35), Box(left=882, top=576, width=34, height=35), Box(left=916, top=576, width=34, height=35), Box(left=951, top=576, width=34, height=35)],
  [Box(left=674, top=611, width=34, height=35), Box(left=708, top=611, width=34, height=35), Box(left=743, top=611, width=34, height=35), Box(left=778, top=611, width=34, height=35), Box(left=812, top=611, width=34, height=35), Box(left=847, top=611, width=34, height=35), Box(left=882, top=611, width=34, height=35), Box(left=916, top=611, width=34, height=35), Box(left=951, top=611, width=34, height=35)]
]

# TODO: medium

# TODO: hard

# TODO: evil


