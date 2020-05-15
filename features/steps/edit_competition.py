from behave import *

use_step_matcher("parse")


@when('I edit the competition with name "{title}"')
def step_impl(context, title):
    """
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:edit', pk=comp.pk))
    form = context.browser.find_by_tag('form')
    if form:
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        context.browser.find_by_value('update').first.click()


@when('I want to edit the competition with name "{title}"')
def step_impl(context, title):
    """
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:edit', pk=comp.pk))



