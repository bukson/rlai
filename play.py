import copy

from game import CpuGame, QLearningCPU, P1, P2, RandomCpu, MinMaxCpu

if __name__ == '__main__':
    print('Qlearn vs Qlearn')
    game = CpuGame(QLearningCPU(P1, decay=1.0), QLearningCPU(P2, decay=1.0))

    r = 200
    for b in range(r):
        print (b / r, '%')
        for i in range(1000):
            game.play()
        game.print_score()
        game.reset_score()
    cpu2 = copy.deepcopy(game.players[P2])
    cpu1 = copy.deepcopy(game.players[P1])

    # cpu2.epsilon = 0
    # cpu2.min_epsilon = 0
    # print('Random vs Qlearn')
    # game = CpuGame(RandomCpu(P1), copy.deepcopy(cpu2))
    # for i in range(20000):
    #     game.play()
    # game.print_score()
    # game.reset_score()

    cpu2.epsilon = 0
    cpu2.min_epsilon = 0
    print('Minmax vs Qlearn')
    game = CpuGame(MinMaxCpu(P1), copy.deepcopy(cpu2))
    for i in range(1000):
        game.play()
    game.print_score()
    game.reset_score()