def calculate_run_rate(runs, balls):
    if balls == 0:
        return 0
    overs = balls / 6
    return round(runs / overs, 2)
