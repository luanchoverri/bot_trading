import datetime
import backtrader as bt

class BacktestManager:
    def __init__(self, datapath, cash=100000.0, fromdate=datetime.datetime(2000, 1, 1), todate=datetime.datetime(2000, 12, 31)):
        self.cerebro = bt.Cerebro()
        self.datapath = datapath
        self.cash = cash
        self.fromdate = fromdate
        self.todate = todate

    def add_data(self):
        data = bt.feeds.YahooFinanceCSVData(
            dataname=self.datapath,
            fromdate=self.fromdate,
            todate=self.todate,
            reverse=False)
        self.cerebro.adddata(data)

    def add_strategy(self, strategy):
        self.cerebro.addstrategy(strategy)

    def run(self):
        self.cerebro.broker.setcommission(commission=0.001)

        self.cerebro.broker.setcash(self.cash)
        print('Starting Portfolio Value: %.2f' % self.cerebro.broker.getvalue())
        self.cerebro.run()
        print('Final Portfolio Value: %.2f' % self.cerebro.broker.getvalue())

        self.cerebro.plot()