import click

from src.robbo_olympic import RobboOlympic


@click.command(name='at', help='Align test')
def align_test():
    ro = RobboOlympic()

    print('That\'s all')
