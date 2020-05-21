from behave import *

use_step_matcher("parse")


@step('Exists competition registered by "{username}"')
def step_impl(context, username):
    """
    :type user: str
    :type context: behave.runner.Context
    """
    from apps.account.models import LeagueUser
    user = LeagueUser.objects.get(username=username)
    for row in context.table:
        get_competition(row, user)


def get_competition(row, user=None):
    import datetime
    from apps.league.models import Competition
    d_format = "%Y-%m-%d %H:%M:%S"
    title = row['title']
    desc = row['description']
    si = datetime.datetime.strptime(f'{row["data_start_inscription_0"]} {row["data_start_inscription_1"]}', d_format)
    fi = datetime.datetime.strptime(f'{row["data_finish_inscription_0"]} {row["data_finish_inscription_1"]}', d_format)
    sc = datetime.datetime.strptime(f'{row["data_start_competition_0"]} {row["data_start_competition_1"]}', d_format)
    fc = datetime.datetime.strptime(f'{row["data_finish_competition_0"]} {row["data_finish_competition_1"]}', d_format)
    comp = Competition.objects.create(title=title, description=desc, data_start_inscription=si, owner=user,
                                      data_finish_inscription=fi, data_start_competition=sc, data_finish_competition=fc)
    comp.save()


