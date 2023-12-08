def rank_up(initial_rank, progress):
    if initial_rank < 0 and initial_rank + progress >= 0:
        new_rank = initial_rank + progress + 1
    else:
        new_rank = initial_rank + progress
    if new_rank > 8:
        new_rank = 8
    return new_rank


class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, activity_rank):
        rank_difference = activity_rank - self.rank
        if activity_rank * self.rank < 0:
            rank_difference -= 1
        if rank_difference == 0:
            gained_points = 3
        if rank_difference == -1:
            gained_points = 1
        if rank_difference > 0:
            gained_points = 10 * (rank_difference ** 2)

        ranks_gained = (self.progress + gained_points) // 100
        self.rank = rank_up(self.rank, ranks_gained)
        self.progress = (self.progress + gained_points) % 100
