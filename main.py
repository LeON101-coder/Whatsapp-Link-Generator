#!/usr/bin/env python
# -*- coding:utf-8 -*-
# WhatsApp Link Generator

import os;
import sys;
from time import sleep;

class Command_prompt:
	def __init__(self):
		self.command_prompt = '\033[0m @console > ';
		print()
		print(" Whatsapp Link Generator ");
		print("-------------------------");
		print("     Coded by: LeON	  ");
		print()
		self.command_line(self.command_prompt);

	def command_line(self, prompt):
		global number;
		global message;
		while True:
			self.c_line = input(prompt.center(5));
			if self.c_line == "":
				pass;
			elif self.c_line in ['show help']:
				print();
				print(" Note: WhatsApp Link Generator for send a message without save the number");
				print(" Usage: command_options");
				print();
				print("Command Options:");
				print("   show help			   Show help options");
				print("   exit				   Exit the programs");
				print("   add number [number] 		   Add a number");
				print("   add message [message]	   Add message");
				print("   show result			   Show result link");
				print();
				print("   Note: The [number] type first with code country ex: 628123xxxxx");
				print("   Note: The [message] use symbol '+' or '%20' for space");
				print();
			elif self.c_line in ['exit']:
				exit("succ: Exit the programs!");
			elif 'add number' in self.c_line:
				number = self.c_line.split()[(-1)];
				if number == "":
					print("err: Error!");
				else:
					pass;
			elif 'add message' in self.c_line:
				message = self.c_line.split()[(-1)];
				if message == "":
					print("err: Error!");
				else:
					pass
			elif self.c_line in ['show result']:
				try:
					number = number;
				except NameError:
					number = 'Null';
				try:
					message = message;
				except NameError:
					message = 'Null';
				if number == 'Null' or message == 'Null':
					link = 'Null';
				else:
					link = f'https://api.whatsapp.com/send?phone={number}&text={message}';
				print();
				print(f" Phone   : {number} ");
				print(f" Message : {message}");
				print(f" Link    : {link}   ");
				print();
				print(" Note: Paste the link in your browser");
				print();
			else:
				print(f"err: '{self.c_line}' command not found");
				print("tip: 'show help' for show help options");

if __name__=='__main__':
	try:
		cho = open('save').read();
	except IOError:
		wrt = open('save', 'a');
		wrt.write('LeON');
		wrt.close();
	try:
		os.system('clear');
		Command_prompt();
	except (KeyboardInterrupt, EOFError):
		exit("succ: Exiting...");