from celery.decorators import task


@task()
def foo(object):
    object.do_some_calculation()