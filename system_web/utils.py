from django.shortcuts import render


def msg(request, string):
	return render(request, 'msg_success.html', {'msg': string})