"""saitama"""
import math

def calculate(times_need, per_day):
    """calculate"""
    days_use = math.ceil(times_need / per_day)
    return days_use
def saitama():
    """saitama workout"""
    push_ups = int(input())
    situp = int(input())
    updown = int(input())
    run = int(input())
    push_ups_perday = int(input())
    situp_perday = int(input())
    run_perday = int(input())
    updown_perday = int(input())
    pu_days_need = calculate(push_ups, push_ups_perday)
    su_days_need = calculate(situp, situp_perday)
    ud_days_need = calculate(updown, updown_perday)
    run_days_need = calculate(run, run_perday)
    if pu_days_need >= su_days_need and pu_days_need >= ud_days_need and\
        pu_days_need >= run_days_need:
        result = pu_days_need
    elif su_days_need >= pu_days_need and su_days_need >= ud_days_need and\
        su_days_need >= run_days_need:
        result = su_days_need
    elif ud_days_need >= pu_days_need and ud_days_need >= su_days_need and\
        ud_days_need >= run_days_need:
        result = ud_days_need
    elif run_days_need >= pu_days_need and run_days_need >= su_days_need and\
    run_days_need >= ud_days_need:
        result = run_days_need
    print(result)
saitama()
