import os
import sys
import subprocess


def record_setting(out):
    """Record scripts and commandline arguments"""
    out = out.split()[0].strip()
    source = out + "/source"
    if not os.path.exists(source):
        os.system('mkdir -p %s' % source)
        # os.mkdir(out)

    # subprocess.call("cp *.py %s" % source, shell=True)
    # subprocess.call("cp configs/*.yml %s" % out, shell=True)

    # pythonファイルを階層構造を保って保存
    subprocess.call("find . -name '*.py' -print0| xargs -0 cp --parents -p -t %s" % source, shell=True)
    subprocess.call("find . -name '*.yml' -print0| xargs -0 cp --parents -p -t %s" % source, shell=True)

    with open(out + "/command.txt", "w") as f:
        f.write(" ".join(sys.argv) + "\n")
