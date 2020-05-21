from behave import *

use_step_matcher("parse")


@when('I register team "{team_name}" at competition "{title}"')
def step_impl(context, team_name, title):
    """
    :type team_name: str
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition, Team
    from time import sleep
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:detail', pk=comp.pk))
    sleep(1)
    print(context.browser.html)
    context.browser.find_by_name('create_team').first.click()
    sleep(1)
    print(context.browser.url)
    assert context.browser.url == context.get_url('competition:create-team', pk=comp.pk)
    context.browser.fill('name', team_name)
    context.browser.find_by_name('sign_up_team').first.click()


@when('I want to register a team at competition "{title}"')
def step_impl(context, title):
    """
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:create-team', pk=comp.pk))