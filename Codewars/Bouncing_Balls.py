#  CodeWars - Bouncing Balls


def bouncingBall(h, bounce, window):

    if h > 0 and 0 < bounce < 1 and window < h:

        x = 0
        while h * bounce ** x > window:
            x += 1

        return x * 2 - 1

    else:
        return -1


print(bouncingBall(3, 0.66, 1.5))
print(bouncingBall(30, 0.66, 1.5))
print(bouncingBall(3, 1, 1.5))
