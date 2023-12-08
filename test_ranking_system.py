from ranking_system import User


def test_user():
    user = User()
    assert user.rank == -8
    assert user.progress == 0
    user.inc_progress(-7)
    assert user.rank == -8
    assert user.progress == 10
    user.inc_progress(-8)
    assert user.rank == -8
    assert user.progress == 13
    user.inc_progress(-5)
    assert user.rank == -7
    assert user.progress == 3
    user.inc_progress(-4)
    assert user.rank == -7
    assert user.progress == 93
    user.inc_progress(-4)
    assert user.rank == -6
    assert user.progress == 83

