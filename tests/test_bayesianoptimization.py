from humpday.optimizers.bayesoptcube import BAYESOPT_OPTIMIZERS
from humpday.objectives.classic import CLASSIC_OBJECTIVES
import random


def test_bayesianoptimization():
    n_trials = 10
    for n_dim in [2,3]:
        for optimizer in BAYESOPT_OPTIMIZERS:
            objective = random.choice(CLASSIC_OBJECTIVES)
            try:
                optimizer(objective, n_trials=n_trials,n_dim=n_dim,with_count=True)
            except Exception as e:
                print(e)
                raise Exception(optimizer.__name__ + ' fails on ' + objective.__name__)


if __name__=='__main__':
    test_bayesianoptimization()