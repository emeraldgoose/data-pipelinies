import datetime, logging, time
from random import random, randint, choices
from constant import *

kst = datetime.timezone(datetime.timedelta(hours=9))

class LOGGEN:
    def create(self, now: datetime.datetime):
        return self._log_generator(now)

    def _log_generator(self, now: datetime.datetime):
        ip = self._ip_generator()
        date = now.strftime('%d/%b/%Y:%H:%M:%S')+' +0900'
        method = self._method_generator()
        status, uri = self._status_generator()
        ua = self._ua_generator()
        pck_size, time = str(randint(1,4595)), str(randint(5,3000))
        return ' '.join([ip,'- -',f'[{date}]',f'"{method} {uri} HTTP/1.1"', status, pck_size, time, f'"{BASE_URL}"', f'"{ua}"'])

    def _ip_generator(self):
        return str(randint(203,223))+'.'+str(randint(2,254))+'.'+str(randint(0,255))+'.'+str(randint(0,255))

    def _method_generator(self):
        return choices(['GET','POST','UPDATE','PUT','DELETE'], weights = [0.6, 0.3, 0.06, 0.03, 0.01])[0]

    def _status_generator(self):
        r1,r2,r3 = random(), randint(0,len(URI)-1), randint(0,len(WRONG_URI)-1)
        m1, m2 = URI[r2], WRONG_URI[r3]
        if r1 > 0.1:
            status, msg = choices(((200,m1),(302,m1)), weights=[0.8, 0.2])[0]
        else:
            status, msg = choices(((404,m2),(401,m1),(403,m1)), weights=[0.8, 0.1, 0.1])[0]
        return str(status), msg

    def _ua_generator(self):
        a1,a2 = ['windows','linux','mac','android','iphone'], ['firefox','opera','chrome','edge','safari']
        b = PLATFORM[a1[randint(0,4)]]
        c = b[randint(0,len(b)-1)]
        return f'Mozilla/5.0 ({c}) {UA[a2[randint(0,4)]]}'


if __name__ == "__main__":
    m = LOGGEN()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    while 1:
        now = datetime.datetime.now(kst)
        for handler in logger.handlers:
            logger.removeHandler(handler)
        file_handler = logging.FileHandler(f"/var/log/httpd/access_log/{now.strftime('%d-%m-%Y-%H')}.log")
        logger.addHandler(file_handler)
        log = m.create(now)
        logger.info(log)
        time.sleep(1)
