N = int(input())
mlist = []

while N!=0:

	for i in range (N):
		mlist.append(int(input()))
	media = (sum (mlist))/N

	resultado=0


	for i in range (N):
		if(mlist[i]>media):
			aux = mlist[i] - media
			mlist[i] = media
			resultado+=aux

	print(resultado)
	mlist.clear()
	N = int(input())
