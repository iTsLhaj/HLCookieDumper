
import os
import io
import dill
import platform
import inquirer
import browser_cookie3

from resources import const
from http.cookiejar import CookieJar
from colored import fg, attr

__author__ = ['iiTs Lhaj']
__version__ = '0.0.1r.0' # first release


class CookieDumpper(object):

    def __init__(self) -> None:

        self.linux_ = platform.system() == 'Linux'
        self.cleanscrn(self.linux_)

        # is user exists
        # get all ids from file

        self.ids_ = []
        for cjFile in os.listdir('cookies'):
            id_ = str(cjFile).replace('cjar_', '')
            id_ = id_.replace('.bin', '')
            self.ids_.append(id_)
        
        self.getCookies(
            browser=self.pickOpt())
        
        print('\n')

    def dump_(self, Cookies: CookieJar) -> None:

        self.cleanscrn(self.linux_, 1)

        # check if cookies dir exists
        if not os.path.exists('./cookies'):
            os.mkdir('cookies')
        
        for cookie in Cookies:
            if cookie.name == 'account_id':
                print(f"[{fg(94)}+{attr(0)}] id: {cookie.value}")

                if cookie.value in self.ids_:
                    filep = f"./cookies/cjar_{cookie.value}.bin"
                    print(f"[{fg(94)}+{attr(0)}] saved in: {filep}")
                
                with io.open(file=f'./cookies/cjar_{cookie.value}.bin', mode='wb') as fS:
                    dill.dump(obj=Cookies, file=fS)

                break

    def getCookies(self, browser: str) -> CookieJar:
        
        if browser.lower() == 'chrome':
            return self.dump_(browser_cookie3.chrome(domain_name=const.DOMAIN_NAME))
        elif browser.lower() == 'firefox':
            return self.dump_(browser_cookie3.firefox(domain_name=const.DOMAIN_NAME))
        elif browser.lower() == 'edge':
            return self.dump_(browser_cookie3.edge(domain_name=const.DOMAIN_NAME))
        else:
            return None
    
    def pickOpt(self) -> str:

        opts = [
            inquirer.List(
                "browser",
                message="What browser u've logged into hoyolab?",
                choices=["chrome", "firefox", "edge"],
            ),
        ]

        return inquirer.prompt(opts)["browser"]

    def cleanscrn(self, unix: bool, nl = 0):

        if unix:
            os.system('clear')
        else:
            os.system('cls')

        if nl != 0:
            print('\n'*nl)


CLI = CookieDumpper