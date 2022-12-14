ps = 'a123456'
time = 1
while time <= 3:
	tps = input('請輸入密碼:')
	if tps == ps:
		print('登入成功')
		break
	else:
		if time == 3:
			print('登入失敗!!')
			break
		else:	
			print('密碼錯誤! 還有', 3-time , '次機會')
			time +=	1
		

