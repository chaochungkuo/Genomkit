class GRegion:
    __slot__ = ["sequence", "start", "end", "orientation", "name", "score",
                "data"]

    def __init__(self, sequence: str, start: int, end: int,
                 orientation: str = ".",
                 name: str = "", score: float = 0, data: list = []):
        self.sequence = sequence
        self.start = start
        self.end = end
        self.orientation = orientation
        self.name = name
        self.score = score
        self.data = data

    def __len__(self):
        return abs(self.start - self.end)

    def __str__(self):
        return "{}:{}-{} {} {}".format(self.sequence,
                                       str(self.start), str(self.end),
                                       self.orientation, self.name)

    def __hash__(self):
        return hash((self.sequence, self.start,
                     self.end, self.orientation))

    def __eq__(self, other):
        return (self.sequence, self.start, self.end, self.orientation) == \
               (other.sequence, other.start, other.end, other.orientation)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.sequence, self.start, self.end) < \
               (other.sequence, other.start, other.end)

    def __le__(self, other):
        return (self.sequence, self.start, self.end) <= \
               (other.sequence, other.start, other.end)

    def __gt__(self, other):
        return (self.sequence, self.start, self.end) > \
               (other.sequence, other.start, other.end)

    def __ge__(self, other):
        return (self.sequence, self.start, self.end) >= \
               (other.sequence, other.start, other.end)

    def extend(self, upstream: int, downstream: int,
               strandness: bool = False, inplace: bool = True):
        """Extend GRegion region the given extension length.
        """
        if strandness:
            if self.orientation == "-":
                new_start = max(0, self.start - downstream)
                new_end = self.end + upstream
            else:  # + or .
                new_start = max(0, self.start - upstream)
                new_end = self.end + downstream

        if inplace:
            self.start = new_start
            self.end = new_end
        else:
            return GRegion(sequence=self.sequence, start=new_start,
                           end=new_end, name=self.name,
                           orientation=self.orientation, data=self.data)

    def extend_percentage(self, upstream: float, downstream: float,
                          strandness: bool = False, inplace: bool = True):
        """Extend GRegion region the given extension length in percentage.
        """
        upstream_length = int(len(self)*upstream)
        downstream_length = int(len(self)*downstream)
        self.extend(upstream=upstream_length, downstream=downstream_length,
                    strandness=strandness, inplace=inplace)

    def overlap(self, region, strandness=False):
        """Return True, if GRegion overlaps with the given region, else False.
        """
        if region.sequence == self.sequence:
            if self.start <= region.start:
                if self.end > region.start:
                    if not strandness:
                        return True
                    elif self.orientation == region.orientation:
                        return True
            else:
                if self.start < region.end:
                    if not strandness:
                        return True
                    elif self.orientation == region.orientation:
                        return True
        return False

    def distance(self, region):
        """Return the distance between two GRegions. If overlapping, return 0;
        if on different chromosomes, return None.
        """
        if self.sequence == region.sequence:
            if self.overlap(region):
                return 0
            elif self < region:
                return region.start - self.end
            else:
                return self.start - region.end
        else:
            return None
