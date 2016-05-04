from importlib import reload
#from imp import reload
#
from time import sleep

import ch10_reload_module

while True:
    print('-' * 20)
    print(ch10_reload_module.pi)
    print(ch10_reload_module.data)
    print(ch10_reload_module.foo(3, 4))
    sleep(5)
    reload(ch10_reload_module)
