from datetime import *

def add_gigasecond(current):
    ts = timedelta(seconds=1000000000)
    gig = ts + current
    return gig
