import random

class AddressBook:

	def __init__(self):
		self.contact_list = []

	def create_contact():
		pass

	def add_contact(self):
		index = random.randint(1, 1000)
		while self.find(index):
			index = random.randint(1, 1000)

		first = raw_input("Enter the first name:")
		last = raw_input("Enter the last name:")
		phonenumber = raw_input("Enter the phonenumber:")
		email = raw_input("Enter the email:")

		contact = {'index': index, 'first': first, 'last': last, 'phonenumber': phonenumber, 'email': email}
		self.contact_list.append(contact)
		print contact
		return contact['index']

	def print_contacts(self):
		for contact in self.contact_list:
			print contact
	
	def count(self):
		return len(self.contact_list)

	def delete(self):
		index = int(raw_input("Enter the index of the contact you wish to delete:"))
		for contact in self.contact_list:
			if contact['index'] == index:
				self.contact_list.remove(contact)
				return
		else:
			print "contact not found."

	def find(self, index):
		for contact in self.contact_list:
			if contact['index'] == index: return True
		return False	

	def modify(self):	
		ri = raw_input("Enter the contact id and key-value, 'id key value':")
		l = ri.split()
		for contact in self.contact_list:
			if contact['index'] == int(l[0]):
				if contact.has_key(l[1]):
					contact[l[1]] = l[2]
					print contact
				else:
					print 'key not found.'
				return 
		print 'Contact not found.'

	def search(self):
		search_str = raw_input("Enter first, last, phone, or email:")		
		if self.contact_list:
			match = 0
			for contact in self.contact_list:
				for key in contact:
					if (contact[key] == search_str):
						print contact
						match += 1
			if match == 0:
				print 'Contact not found' 
		else: 
			print 'Contact not found'


if __name__ == '__main__':

	a = AddressBook()

	while True:
		option =  raw_input("Add(a) Modify(m) Print(p) Search(s) Delete(d):")
	
		if option == 'a':
			a.add_contact()
		elif option == 'd':
			a.delete()
		elif option == 's':
			a.search()
		elif option == 'm':
			a.modify()
		elif option == 'p':
			a.print_contacts()
		else:
			print "No option given..."