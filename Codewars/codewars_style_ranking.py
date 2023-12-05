# [Training on Codewars style ranking system](https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python)

# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method


RANKS: list[int] = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]


class User:
    def __init__(self, rank: int = -8, progress: int = 0) -> None:
        self.rank = rank
        self.progress = progress

    def inc_progress(self, activity_rank: int):
        if self.rank in [0, 8]:
            return
        if self.rank > activity_rank:
            if self.rank - activity_rank == 1:
                self.progress += 1
        elif self.rank == activity_rank:
            self.progress += 3
        elif activity_rank > self.rank:
            d = RANKS.index(activity_rank) - RANKS.index(self.rank)
            self.progress += 10 * d**2

        if self.progress > 99:
            self.rank += self.progress // 100
            self.progress = self.progress - self.progress // 100 * 100


# user = User()
# user.rank # => -8
# user.progress # => 0
# user.inc_progress(-7)
# user.progress # => 10
# user.inc_progress(-5) # will add 90 progress
# user.progress # => 0 # progress is now zero
# user.rank # => -7 # rank was upgraded to -7
