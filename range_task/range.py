class Range:
    def __init__(self, start: float, end: float) -> None:
        self.__start = start
        self.__end = end

    @property
    def start(self) -> float:
        return self.__start

    @start.setter
    def start(self, start: float) -> None:
        self.__start = start

    @property
    def end(self) -> float:
        return self.__end

    @end.setter
    def end(self, end: float) -> None:
        self.__end = end

    @property
    def length(self) -> float:
        return self.__end - self.__start

    def is_inside(self, number: float) -> bool:
        return self.__start <= number <= self.__end

    def get_interval_intersection(self, other):
        if self.__end < other.__start or self.__start > other.__end:
            return None
        return [max(self.__start, other.__start), min(self.__end, other.__end)]

    def get_interval_union(self, other):
        if self.__end < other.__start or self.__start > other.__end:
            return [(self.__start, self.__end), (other.__start, other.__end)]
        return [min(self.__start, other.__start), max(self.__end, other.__end)]

    def get_interval_difference(self, other):
        if self.get_interval_intersection(other) is None:
            return None
        if self.start < other.start:
            return [self.start, other.start]
        if self.end > other.end:
            return [other.end, self.end]
