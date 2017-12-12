#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys, os, os.path
import subprocess, optparse, time, re


def shell(cmd, env=None):
    new_env = os.environ.copy()
    if env:
        for k in env:
            new_env[k] = env.get(k)

    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=new_env)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        print
        output
        raise subprocess.CalledProcessError(retcode, cmd)
    return output


def tomcat_pid_jps(base):
    try:
        output = shell("jps -v|grep catalina.base=" + base)
        for line in output.split('\n'):
            if line.find('base') >= 0:
                return re.split('\\s+', line)[0]
    except subprocess.CalledProcessError:
        pass


def tomcat_pid_ps(base):
    output = shell("ps -efww|grep catalina.base=" + base)
    for line in output.split('\n'):
        if line.find('java') >= 0:
            return re.split('\\s+', line)[1]
    return None


def command_start(opt, args):
    output = shell("nohup %s/bin/startup.sh &" % opt.tomcat, {'CATALINA_BASE': opt.base, 'JAVA_HOME': opt.home})
    # 等待一段时间并检测进程是否还存在
    for i in range(5):
        time.sleep(1)
        pid = tomcat_pid_ps(opt.base)
        if pid:
            return

    raise Exception('startup 失败:' + output + 'env=' + str(os.environ))


def command_stop(opt, args):
    pid = tomcat_pid_ps(opt.base)
    if not pid:
        return

    shell("%s/bin/shutdown.sh" % opt.tomcat, {'CATALINA_BASE': opt.base, 'JAVA_HOME': opt.home})

    # 等待一段时间并检测进程是否还存在
    for i in range(5):
        pid = tomcat_pid_ps(opt.base)
        if not pid:
            return
        time.sleep(3)

    if opt.force:
        shell("kill -9 %s" % pid)
    else:
        raise Exception('shutdown 失败')


def parse_arg():
    parser = optparse.OptionParser(usage="usage: tomcat-ctl <command> [<args>]")
    parser.add_option("-b", "--base", dest="base", help="path to CATALINA.BASE", metavar="CATALINA.BASE")
    parser.add_option("-t", "--tomcat", dest="tomcat", help="path to CATALINA.HOME", metavar="CATALINA.HOME")
    parser.add_option("-j", "--home", dest="home", help="path to JAVA.HOME", metavar="JAVA.HOME")
    parser.add_option("--force", dest="force", action="store_true", help="force kill tomcat if shutdown failed",
                      metavar="CATALINA.HOME")

    if len(sys.argv) < 2:
        parser.print_help()
        return None

    cmd = sys.argv[1]
    result = parser.parse_args(sys.argv[1:])

    if not result[0].tomcat:
        if os.environ.has_key('CATALINA_HOME'):
            result[0].tomcat = os.environ['CATALINA_HOME']
        else:
            raise Exception('需指定-t 或者设置环境变量CATALINA.HOME')
    result[0].tomcat = os.path.normpath(result[0].tomcat)

    if not result[0].base:
        if os.environ.has_key('CATALINA_BASE'):
            result[0].base = os.environ['CATALINA_BASE']
        else:
            result[0].base = result[0].tomcat
    result[0].base = os.path.normpath(result[0].base)

    return cmd, result[0], result[1]


arg = parse_arg()
print(arg)
if arg is not None:
    cmd, opt, args = arg
    eval('command_' + cmd)(opt, args)

# scripts / tomcat - ctl start - t {{dir}} / {{tomcat}} - b {{dir}} / {{tomcat}} - j {{java_home}}
