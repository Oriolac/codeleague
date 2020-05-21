from behave import *

use_step_matcher("parse")


@when('I delete the competition with name "{title}"')
def step_impl(context, title):
    """
    :param context:
    :type title: str
    """
    from apps.league.models import Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:detail', pk=comp.pk))
    context.browser.find_by_name(f'delete_competition').first.click()
    print(context.browser.html)
    assert context.browser.url == context.get_url('competition:delete', pk=comp.pk)
    form = context.browser.find_by_tag('form')
    context.browser.find_by_name('confirm').first.click()


@then('The list contains {count:n} competition')
def step_impl(context, count):
    """
    :param context:
    :type count: str
    """
    from apps.league.models import Competition
    assert 1 == Competition.objects.all().__len__()


@when('I want to delete the competition "{name}"')
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition
    comp = Competition.objects.all().get(title=name)
    context.browser.visit(context.get_url('competition:delete', pk=comp.pk))