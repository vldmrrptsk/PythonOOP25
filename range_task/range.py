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

    def get_intersection(self, other):
        left_border = max(self.__start, other.__start)
        right_border = min(self.__end, other.__end)

        if left_border >= right_border:
            return None

        return Range(left_border, right_border)

    def get_union(self, other):
        if self.__end < other.__start or self.__start > other.__end:
            return [Range(self.__start, self.__end), Range(other.__start, other.__end)]

        return [Range(min(self.__start, other.__start), max(self.__end, other.__end))]

    def get_difference(self, other):
        if self.__end <= other.__start or self.__start >= other.__end:
            return [Range(self.__start, self.__end)]

        if other.__start <= self.__start and other.__end >= self.__end:
            return []

        if other.__start <= self.__start:
            return [Range(other.__end, self.__end)]

        if other.__end >= self.__end:
            return [Range(self.__start, other.__start)]

        return [
            Range(self.__start, other.__start),
            Range(other.__end, self.__end)
        ]

    def __repr__(self) -> str:
        return f"Range({self.start}, {self.end})"
