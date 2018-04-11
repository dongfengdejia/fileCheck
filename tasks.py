from invoke import task
from nose import run as noserun

readMe = "README.md"

@task
def help():
    lines = open(readMe, "r").read().split("##")
    for line in lines:
        if line.strip().startswith("usage"):
            print "## " + line
            break

# @task            
# def test(ctx):
    # result = ctx.run("python test_fileCheck.py")
    # print "+++", result, "+++"
    # print "+++", result.ok
    # assert result.ok is True
    
@task            
def test(ctx):
    result = noserun(argv=['', '--m=^test_'])
    assert result is True