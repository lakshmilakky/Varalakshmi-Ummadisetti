person = input ("Enter Person Name:")
movie_name = input ("Enter Movie Name:") 
theatre_name = input ("Enter Theatre Name:")
txt = "{person} went to {movie_name} movie at {theatre_name} theatre"
print(txt.format(person=person, movie_name=movie_name, theatre_name=theatre_name)) 
