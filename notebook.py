#coding:MS950

import tkinter as tk
import pickle as pkl
import os
from tkinter import messagebox

window=tk.Tk()
window.title('�O�ƥ�')
window.geometry('400x400')

name=tk.Entry(window,width=200)
name.pack(ipady=10)

event=tk.Entry(window,width=200)
event.pack(ipady=10)

l=tk.Label(window,text= \
			'²���O�ƥ��{��,\n�R���ƥ�Цb�Ĥ@�奻�ؤ���J�W��,\n��ܨƥ���U���s��|��ܩ��Lwindow\n', \
			bg='pink',font=('Arial',12), \
			width=200,height=10)
l.pack()

def show():
	labels=[]
	windowshow=tk.Tk()
	windowshow.title('�M��')
	windowshow.geometry('400x400')
	lb=tk.Listbox(windowshow,width=400,height=400)
	lb.pack()
	for root,dirs,files in os.walk(r'D:\notebook'):
		for name in files:
			try:
				y=open(os.path.basename(name),'rb')
				data=pkl.load(y)
				for k,v in data.items():
					lb.insert('end',k+' '+v)				
				else:
					y.close()
			except (pkl.UnpicklingError,FileNotFoundError):
				pass
		else:
			pass
	else:
		pass
	windowshow.mainloop()


def savemethod():
	x=None
	filename=''
	data={'�W��':str(name.get()),'�ƥ�':str(event.get())}
	filename=name.get()+'.pkl'
	x=open(filename,'wb')
	pkl.dump(data,x)
	if x is not None:
		messagebox.showinfo(title='���\',message='�Ыئ��\!')
		x.close()


def remove():
	x=name.get()+'.pkl'
	try:
		os.remove(x)
	except FileNotFoundError:
		print(messagebox.showerror())
	else:
		print(messagebox.showinfo(title='���\',message='�R�����\!'))
	


button1=tk.Button(window,text='�[�J�ƥ�',width=150,height=2,command=savemethod)
button1.pack()

button2=tk.Button(window,text='��ܨƥ�',width=150,height=2,command=show)
button2.pack()

button3=tk.Button(window,text='�R���ƥ�',width=150,height=2,command=remove)
button3.pack()




window.mainloop()
