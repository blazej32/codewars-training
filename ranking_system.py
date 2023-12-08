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
        possible_ranks = [-8, -7, -6, -5, -4, -3, -2,
                          -1, 1, 2, 3, 4, 5, 6, 7, 8]
        if activity_rank not in possible_ranks:
            raise ValueError
        rank_difference = activity_rank - self.rank
        gained_points = 0
        if activity_rank * self.rank < 0:
            if rank_difference > 0:
                rank_difference -= 1
            elif rank_difference < 0:
                rank_difference += 1
        if rank_difference == 0:
            gained_points += 3
        if rank_difference == -1:
            gained_points += 1
        if rank_difference > 0:
            gained_points += 10 * (rank_difference ** 2)

        ranks_gained = (self.progress + gained_points) // 100
        self.rank = rank_up(self.rank, ranks_gained)
        if self.rank == 8:
            self.progress = 0
        else:
            self.progress = (self.progress + gained_points) % 100
