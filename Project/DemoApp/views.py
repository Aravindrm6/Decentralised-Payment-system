from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,'index.html')
def hi(request):
	return render(request,'DEMOAPP/hi.html')
def new(request):
	return render(request,'DEMOAPP/like_button.js')
def lo(request):
	return render(request,'DEMOAPP/login.html')
def sty(request):
	return render(request,'DEMOAPP/style.css')
def hello(request):
	p=int(request.POST["p"])
	context={
	"p":p
	}
	return render(request,'DEMOAPP/hi.html',context)
def login(request):
	import warnings
	user=str(request.POST["user"])
	password=str(request.POST["pass"])
	m={}
	m['aravind,aravi1995']=0
	m['aravind,aravi1996']=1
	m['aravind,aravi1997']=2
	x=user+','+password
	if x in m:
		context={
		"p":m[x]
		}
		return render(request,'DEMOAPP/hi.html',context)
	context={'in':"invalid credentials"}
	return render(request,'index.html',context)
def timelog(request):
	
	from web3 import Web3
	import json
	'''fname=str(request.POST["fname"])
	'''
	ganache="http://127.0.0.1:7545"
	web3=Web3(Web3.HTTPProvider(ganache))
	id1=int(request.POST["p"])
	web3.eth.defaultAccount=web3.eth.accounts[id1]
	abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"distance","type":"uint256"}],"name":"generateBill","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"e","type":"string"}],"name":"getDistance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusLocation","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusPrice","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusTime","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getVehicle","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getindex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"price","type":"uint256"}],"name":"regVehicle","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"reg_vehicle","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_Location","type":"string"}],"name":"updateLocation","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"vehicleMapping","outputs":[{"internalType":"uint256","name":"vid","type":"uint256"},{"internalType":"address","name":"vehicle","type":"address"},{"internalType":"uint256","name":"price_per_km","type":"uint256"},{"internalType":"uint256","name":"time","type":"uint256"},{"internalType":"uint256","name":"price","type":"uint256"}],"stateMutability":"view","type":"function"}]')
	address=web3.toChecksumAddress("0xF3032BD7fbd8Bb5f5Fc355fb2903DF2fd9Ba42F6")
	contract=web3.eth.contract(address=address,abi=abi)
	tx=contract.functions.getStatusTime().call()
	print(tx)
	context={}
	v={}
	for i in range(len(tx)):
		v[i]=tx[i]
	context['q']=v
	context['p']=id1
	return render(request,'result.html',context)
def locationlog(request):
	
	from web3 import Web3
	import json
	ganache="http://127.0.0.1:7545"
	web3=Web3(Web3.HTTPProvider(ganache))
	id1=int(request.POST["p"])
	web3.eth.defaultAccount=web3.eth.accounts[id1]
	abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"distance","type":"uint256"}],"name":"generateBill","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"e","type":"string"}],"name":"getDistance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusLocation","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusPrice","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusTime","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getVehicle","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getindex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"price","type":"uint256"}],"name":"regVehicle","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"reg_vehicle","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_Location","type":"string"}],"name":"updateLocation","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"vehicleMapping","outputs":[{"internalType":"uint256","name":"vid","type":"uint256"},{"internalType":"address","name":"vehicle","type":"address"},{"internalType":"uint256","name":"price_per_km","type":"uint256"},{"internalType":"uint256","name":"time","type":"uint256"},{"internalType":"uint256","name":"price","type":"uint256"}],"stateMutability":"view","type":"function"}]')
	address=web3.toChecksumAddress("0xF3032BD7fbd8Bb5f5Fc355fb2903DF2fd9Ba42F6")
	contract=web3.eth.contract(address=address,abi=abi)
	tx=contract.functions.getStatusLocation().call()
	print(tx)
	context={}
	v={}
	for i in range(len(tx)):
		v[i]=tx[i]
	context['q']=v
	context['p']=id1
	print(context)
	return render(request,'DEMOAPP/file1.html',context)
def reg(request):
	from web3 import Web3
	import json
	fname=int(request.POST["fname"])
	id1=int(request.POST["p"])
	ganache="http://127.0.0.1:7545"
	web3=Web3(Web3.HTTPProvider(ganache))
	web3.eth.defaultAccount=web3.eth.accounts[id1]
	abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"distance","type":"uint256"}],"name":"generateBill","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"e","type":"string"}],"name":"getDistance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusLocation","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusPrice","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusTime","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getVehicle","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getindex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"price","type":"uint256"}],"name":"regVehicle","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"reg_vehicle","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_Location","type":"string"}],"name":"updateLocation","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"vehicleMapping","outputs":[{"internalType":"uint256","name":"vid","type":"uint256"},{"internalType":"address","name":"vehicle","type":"address"},{"internalType":"uint256","name":"price_per_km","type":"uint256"},{"internalType":"uint256","name":"time","type":"uint256"},{"internalType":"uint256","name":"price","type":"uint256"}],"stateMutability":"view","type":"function"}]')
	address=web3.toChecksumAddress("0xF3032BD7fbd8Bb5f5Fc355fb2903DF2fd9Ba42F6")
	contract=web3.eth.contract(address=address,abi=abi)
	contract.functions.regVehicle(fname).transact()
	tx=contract.functions.regVehicle(fname).call()
	print(tx)
	context={
	"tx":tx,
	"p":id1
	}
	return render(request,'DEMOAPP/regist.html',context)
def update(request):
	from web3 import Web3
	import json
	e=str(request.POST["fname"])
	ganache="http://127.0.0.1:7545"
	web3=Web3(Web3.HTTPProvider(ganache))
	p=int(request.POST["p"])
	web3.eth.defaultAccount=web3.eth.accounts[p]
	abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"distance","type":"uint256"}],"name":"generateBill","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"e","type":"string"}],"name":"getDistance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusLocation","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusPrice","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusTime","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getVehicle","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getindex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"price","type":"uint256"}],"name":"regVehicle","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"reg_vehicle","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_Location","type":"string"}],"name":"updateLocation","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"vehicleMapping","outputs":[{"internalType":"uint256","name":"vid","type":"uint256"},{"internalType":"address","name":"vehicle","type":"address"},{"internalType":"uint256","name":"price_per_km","type":"uint256"},{"internalType":"uint256","name":"time","type":"uint256"},{"internalType":"uint256","name":"price","type":"uint256"}],"stateMutability":"view","type":"function"}]')
	address=web3.toChecksumAddress("0xF3032BD7fbd8Bb5f5Fc355fb2903DF2fd9Ba42F6")
	contract=web3.eth.contract(address=address,abi=abi)
	dist=contract.functions.getDistance(e).call()
	if (dist==0):
		contract.functions.updateLocation(e).transact()
	else:
		contract.functions.generateBill(dist).transact()
		contract.functions.updateLocation(e).transact()
	tx=''
	vi="Vehicle ID : "+str(contract.functions.getVehicle().call())+"\n"
	id1="Vehicle Price Status : "+str(contract.functions.getStatusPrice().call())+"\n"
	pr="Vehicle Time Status : "+str(contract.functions.getStatusTime().call())+"\n"
	up=contract.functions.updateLocation(e).call()
	print(tx)
	return render(request,'DEMOAPP/updated.html',{"vi":vi,"id1":id1,"pr":pr,"up":up,"p":p})