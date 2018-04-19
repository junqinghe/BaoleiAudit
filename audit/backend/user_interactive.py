from django.contrib.auth import authenticate

class UserShell(object):
    def  __init__(self,sys_argv):
        self.sys_argv=sys_argv
        self.user=None

    def auth(self):
        count=0
        while count<=3:
            username=input('username:').strip()
            password=input('password:').strip()
            user=authenticate(username=username,password=password)
            #NONE表示不成功
            if not user:
                count+=1
                print('Invalid username or password')
            else:
                self.user=user
                return True
        else:
            print('输入太多次了')

    def start(self):
        if self.auth():
            while True:
                host_groups=self.user.account.hostgroups.all()
                for index,group in enumerate(host_groups):
                    print('%s \t%s[%s]'%(index,group,group.hostuserbinds.count()))
                print('%s \t未分配小组[%s]'%(len(host_groups),self.user.account.hostuserbinds.count()))
                choice=input('select group:').strip()
                host_bind_list=None
                if choice.isdigit():
                    choice=int(choice)
                    if choice>=0 and choice<len(host_groups):
                        select_group=host_groups[choice]
                        host_bind_list=select_group.hostuserbinds.all()
                    elif choice==len(host_groups):
                        host_bind_list=self.user.account.hostuserbinds.all()
                    if host_bind_list:
                        while True:
                            for index,host in enumerate(list(host_bind_list)):
                                print('%s\t%s'%(index,host))
                            choice2 = input('select host:').strip()
                            if choice2.isdigit():
                                choice2=int(choice2)
                                if choice2>0 and choice2<len(host_bind_list):
                                    select_host=host_bind_list[choice2]
                                    print('selected host>>>>',select_host)
                                else:
                                    print('invalid input')
                            elif choice2=='b':
                                break
                            else:
                                print('invalid input')

