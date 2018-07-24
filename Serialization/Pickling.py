import pickle

##example_dict = {1:"1", 2:"4",3:"9"}
##pickle_out = open("dict.pickle","wb")
##pickle.dump(example_dict,pickle_out)
##pickle_out.close()

pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)

print(example_dict)
print(example_dict[2])



