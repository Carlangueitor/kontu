from fabric.api import task, local


@task
def test():
    """
    Run tests.
    """
    local("nosetests --config nose.cfg")
