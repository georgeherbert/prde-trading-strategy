import sys

from BSE import market_session

k = int(sys.argv[1])
f = round(float(sys.argv[2]), 2)

sellers_spec = [('PRDE', 15, {'k': k, 's_min': -1, 's_max': 1, 'F': f})]
buyers_spec = sellers_spec

traders_spec = {'sellers': sellers_spec, 'buyers': buyers_spec}

sup_range = (60, 60)
dem_range = (140, 140)

start_time = 0
end_time = 60 * 60 * 24 * 100
supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [sup_range], 'stepmode': 'fixed'}]
demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [dem_range], 'stepmode': 'fixed'}]

order_interval = 5
order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'drip-jitter'}

trial_id = f'k={k},F={f}'
tdump = open(f'{trial_id}_avg_balance.csv','w')
dump_all = False
verbose = False

market_session(trial_id, start_time, end_time, traders_spec, order_sched, tdump, dump_all, verbose)

tdump.close()