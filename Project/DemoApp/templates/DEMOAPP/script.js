const form=document.getElementById("form")
const Web3=require('web3');
const ganache='http://127.0.0.1:7545'
const web3=new Web3(ganache)
web3.eth.defaultAccount=web3.eth.accounts[0]
const abi=[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"distance","type":"uint256"}],"name":"generateBill","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"e","type":"string"}],"name":"getDistance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusLocation","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusPrice","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStatusTime","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getVehicle","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"price","type":"uint256"}],"name":"regVehicle","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"reg_vehicle","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_Location","type":"string"}],"name":"updateLocation","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"vehicleMapping","outputs":[{"internalType":"uint256","name":"vid","type":"uint256"},{"internalType":"address","name":"vehicle","type":"address"},{"internalType":"uint256","name":"price_per_km","type":"uint256"},{"internalType":"uint256","name":"time","type":"uint256"},{"internalType":"uint256","name":"price","type":"uint256"}],"stateMutability":"view","type":"function"}]
const address="0xd830a3111d68928E73186c7Bdc0FDa6ad933AB7b"
const contract=new web3.eth.Contract(abi,address)
contract.methods.getStatusLocation().call((error,result)=>{console.log(result)})