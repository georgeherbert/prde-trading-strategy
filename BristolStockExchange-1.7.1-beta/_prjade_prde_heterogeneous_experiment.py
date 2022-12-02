import sys

from BSE import market_session

num_prjade = sys.argv[1]
num_prde = 15 - num_prjade

sellers_spec = [
    ('PRJADE', num_prjade, {'k': 14, 's_min': -1, 's_max': 1, 'p': 12.5, 'c': 0.125})
    ('PRDE', num_prde, {'k': 14, 's_min': -1, 's_max': 1, 'F': 0.8})
]
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

trial_id = f'prjade_{num_prjade}_prde_{num_prde}'
tdump = open(f'{trial_id}_avg_balance.csv','w')
dump_all = False
verbose = False

market_session(trial_id, start_time, end_time, traders_spec, order_sched, tdump, dump_all, verbose)

tdump.close()