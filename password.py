password = 'a123456'

user_name = input('請輸入使用者帳號: ')
y = 3

while y > 0:
	y = y - 1
	password_user = input('請輸入使用者密碼: ')
	if password_user == password:
		print('歡迎回來', user_name)
		break
	else:
		print('密碼錯誤!')
		if y > 0:
			print('還有', y, '次機會')
		else:
			print('錯誤過多，請稍後再試')