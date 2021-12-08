import hmac
import hashlib
def get_md5(password,token):
	print(password,' ',token)
	return hmac.new(token.encode(), password.encode(), hashlib.md5).hexdigest()

if __name__=='__main__':
	print(get_md5(None,'1'))