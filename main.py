from __future__ import (absolute_import, division, print_function, unicode_literals)
from test_strategy import TestStrategy
from backtest_manager import BacktestManager
import os.path
import sys

if __name__ == '__main__':

    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, 'data/orcl-1995-2014.txt')

    backtest_manager = BacktestManager(datapath)
    backtest_manager.add_data()
    backtest_manager.add_strategy(TestStrategy)
    backtest_manager.run()
