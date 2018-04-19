from audit.backend import user_interactive
import sys,os

if __name__ =='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baoleiAudit.settings")    #因为不是django的view中，所有要设置环境
    import django
    django.setup()            #注册所有app
    obj=user_interactive.UserShell(sys.argv)
    obj.start()