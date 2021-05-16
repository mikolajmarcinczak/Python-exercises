import datetime as dt
from dateutil import relativedelta as rd

def Elapsed(past_date):
    diff = rd.relativedelta(dt.datetime.now(), past_date)
    return diff.years, diff.months, diff.days

if __name__ == '__main__':
    past_date = dt.datetime(int(input('Wprowadz rok: ')), int(input('Wprowadz miesiac: ')), int(input('Wprowadz dzien: ')))
    yrs, mths, days = Elapsed(past_date)
    print(f'Od wprowadzonej daty uplynelo: {(yrs)} lat, {(mths)} miesiecy i {(days)} dni.')