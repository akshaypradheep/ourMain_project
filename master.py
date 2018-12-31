#!/usr/bin/python3
import pyrebase
#Firebase Configuration
config = {
  "apiKey":"AIzaSyBeTkzdsVpcKpZkU9BMzNwCloUlNf2MWAo",
  "authDomain": "akshaypradheepdc.firebaseapp.com",
  "databaseURL": "https://akshaypradheepdc.firebaseio.com",
  "storageBucket": "akshaypradheepdc.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def reg():
	_name = input("Enter the Name of Card Holder: ")
	_cNo = input("Enter the Card Number: ")
	_noH = input("Enter the number of Heads in family: ")
	_cat = input("Enter whether APL or BPL: ")
	db.child("NAME").child(_cNo).set(_name)
	db.child("NumHead").child(_cNo).set(_noH)
	db.child("Category").child(_cNo).set(_cat)
	pass
def read():
	_cNo = input("Enter the Card Number: ")
	_name = db.child("NAME").child(_cNo).get()
	_cat = db.child("Category").child(_cNo).get()
	_noH = db.child("NumHead").child(_cNo).get()
	name = _name.val()
	cat = _cat.val()
	noH = _noH.val()
	return name,cat,noH
while 1:
	a,b,c = read()
	print("NAME: ",a)
	print("CATEGORY:",b)
	print("NUM OF HEADS",c)

