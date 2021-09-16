print("hello MAC")


def test(domain):
    print('11 domain:', domain)
    print('11 len:', len(domain))
    if len(domain) > 50:
        domain = domain[:50]
        print('22 domain:', domain)
        print('22 len:', len(domain))

domain='www.12345678901234567890123456789012345678901234567a.com'
test(domain)
print('33 domain:', domain)
print('33 len:', len(domain))

domain_cn = '中文域名长度怎么算超过50个是assci还是中文啊从老没有见过中文域名，我们的规则支持吗只有试一下才会自带了'
test(domain_cn)
print('44 domain_cn:', domain_cn)
print('44 domain_cn:', len(domain_cn))
