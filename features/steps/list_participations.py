from behave import *

use_step_matcher("parse")


@when('I view participations of user "{username}"')
def step_impl(context, username):
    """
    :type username: str
    :type context: behave.runner.Context
    """
    from apps.league.models import LeagueUser
    user = LeagueUser.objects.get(username=username)
    context.browser.visit(context.get_url('account:participations', pk=user.id))


@then('I\'m viewing a list of all competitions "{user}" has participated')
def step_impl(context, user):
    """
    :type user: str
    :type context: behave.runner.Context
    """
    for row in context.table:
        assert row['title'] == context.browser.find_by_text(row['title']).first.text

