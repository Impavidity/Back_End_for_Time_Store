# -*-coding:utf-8 -*-

import jpush as jpush
from config import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)

def main():
	push = _jpush.create_push()
	#print dir(push)
	push.audience = jpush.all_
	#print dir(push.message)

	
	#android_msg = jpush.android(alert="Hello, android msg")
	push.message = jpush.message("Fucking Message", title="Hello")
	push.platform = jpush.all_
	push.send()
	

if __name__=="__main__":
	main()