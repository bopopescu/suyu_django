# -*-coding:utf-8 -*-import salt.client as scdef run_cmd(ip,model):    local=sc.LocalClient()    result=local.cmd(ip,model)    return result