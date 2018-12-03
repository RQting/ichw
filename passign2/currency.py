"""exchange.py:Telling you how much you will receive
when you exchange one currency into another
__author__ = "Yuan Changfeng"
__pkuid__  = "1800011838"
__email__  = "1800011838@pku.edu.cn"
"""

def before_space(s):
    first=''
    for i in s:
        if (ord(i)<48 and ord(i)!=46) or ord(i)>57:   
            first=first
        else:
            first=first+i    #去掉非数字但保留'.'
    return float(first)
    
def after_space(s):
    after=''
    for i in s:
        if (ord(i)<48 and ord(i)!=46) or ord(i)>57:    
            after=after+i
    return after
    
def first_inside_quotes(s):
    a1=s.find('"')   #找到第一个'"',a1为第一个'"'的位置
    a2=s[a1+1:].find('"')+a1+1       #取出没有第一个'"'的子字符串,再用find找到第二个'"'，并加上相应的值使a2对应第二个'"'的位置
    first=s[a1+1:a2]
    return first

def get_from(json):
    a1=json.find('"')
    a2=json[a1+1:].find('"')+a1+1         #ai为第i个'"'的位置
    a3=json[a2+1:].find('"')+a2+1
    a4=json[a3+1:].find('"')+a3+1         
    getfrom=json[a3+1:a4]
    return getfrom

def test_get_from():
    assert('3 United States Dollars' == get_from(exchange('USD', 'EUR', 3)))
    
def get_to(json):
    a1=json.find('"')
    a2=json[a1+1:].find('"')+a1+1
    a3=json[a2+1:].find('"')+a2+1
    a4=json[a3+1:].find('"')+a3+1
    a5=json[a4+1:].find('"')+a4+1
    a6=json[a5+1:].find('"')+a5+1
    a7=json[a6+1:].find('"')+a6+1
    a8=json[a7+1:].find('"')+a7+1
    getto=json[a7+1:a8]
    return getto
    
    
def test_get_to():
    assert('2.590707 Euros'==get_to(exchange('USD', 'EUR', 3)))
def has_error(json):
    a1=json.rfind('"')
    a2=json[:len(json)-(len(json)-a1)].rfind('"')  #用rfind反向找到倒数第一个'"',a1,a2为倒数第一，倒数第二个'"'的位置
    if len(json[a2+1:a1])==0:
        return True
    else:
        return False
        
def exchange(currency_from, currency_to, amount_from):
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from)) #to make parameter operational
    docstr = doc.read()          #The contents of this web page as a string.,to get what the form we want
    doc.close()    
    json = docstr.decode('ascii')   #convert the input into the wantedd result
    return(json)
    
 
 
def test_exchange():
    number = before_space(get_to(exchange('USD', 'EUR', 3)))
    assert (number == 2.590707)
    
def test_all():
    test_get_from()
    test_get_to()
    test_exchange()
    print('All tests passed')
    
if __name__ == '__main__':
    currency_from = input('原货币:')
    currency_to = input('目标货币:')
    amount_from = input('原货币数:')
    test_all()
    print(exchange(currency_from, currency_to, amount_from))
