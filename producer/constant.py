URI = ['/api/users', '/api/items', '/api/home', '/api/login', '/']
WRONG_URI = ['/api/usr', '/api/user','/api/itm', '/api/item','/api/loi', '/api/logn', '/api/aaa', '/api/abc', '/api/qwer', '/api/asdf', '/api/zxc']
PLATFORM = {
    'windows' : ['Windows NT 10.0; Win64; x64','Windows NT 6.0; Win64; x64', 'Windows NT 6.1; Win64; x64', 'Windows NT 6.2; Win64; x64', 'Windows NT 6.3; Win64; x64'],
    'linux' : ['X11; Linux x86_64'],
    'mac' : ['Macintosh; Intel Mac OS X; U; en'],
    'android' : [f'Linux; Android {a}.0.1; sdk Build/KK' for a in range(7,14)],
    'iphone' : [f'iPhone; CPU iPhone OS {a}_{0}_{1} like Mac OS X' for a in range(11,17)],
    }
UA = {
    'firefox' : 'Gecko/geckotrail Firefox/firefoxversion', 
    'chrome' : 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'opera' : 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41',
    'edge' : 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59',
    'safari' : 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1',
    }
BASE_URL = 'https://www.dummmmmy.com'