"""
Project Tasks that can be invoked using using the program "invoke" or "inv"
"""

import os
from invoke import task

PROJECT_NAME = 'calc'

@task(default=True)
def lint(ctx):
    """
    Run pylint on files
    """
    files = ' '.join([
        PROJECT_NAME,
        'tasks.py',
    ])
    cmd = 'python3 -m pylint --output-format=parseable {files}'
    cmdf = cmd.format(files=files)
    print(cmdf)
    ctx.run(cmdf, pty=True)

@task
def clean(ctx):
    """
    Clean repository using git
    """
    ctx.run('git clean --interactive', pty=True)
