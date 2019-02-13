=======
Journal
=======

Premier rendu
=============

Création du module Car contenant:
	* Attributs:
		* __color
		* __direction
		* __x
		* __y
		* __size

	* selecteurs:
		* get_color
		* get_size
		* get_direction
		* get_x
		* get_y
		* get_coord
	* predicat:
		* is_over


Création du module Board :
	Module representant un plateau de jeu
	contenant:
	
	* Attribut:
		* __configuration
	
	* Methodes:
		* add_Car

		

	* Selecteur:
		* get_configuration
		* get_list_coord_occupied
		* get_list_of_move
		
	
	* Predicat:
		* conf_is_valid

Deuxieme rendu
==============
	Ajout dans la class Car:
		* Methodes :
			* __eq__
			* __repr__
			* move_car
			* compare

	Ajout et modification dans la class Board:
		* Attributs:
			* __dict_index_of_Cars

		* Selecteur:
			* get_dict_index_of_cars
			* get_list_coord_with_color
			* get_new_board_after_movement	
		* Methode:
			
			* __eq__
			* draw	
			* copy
			

		* Predicat :
			* is_final

		* Modification:
	
			Dans __init__ les voitures stockés dans la configuration sont triés dans l'ordre 				alphabetique inverse, 'Z' etant la voiture rouge il est interessant de l'avoir à 				l'indice 0 de la liste, ce tri est aussi utile dans la comparaison de deux
			configuration d'objets Board.

troisieme rendu
===============
	* Ajout dans la class Car:
		* Methode:
			* __hash__

	* Ajout dans la class Board:
		* Methode:
			* __hash__
			* get_last_movement_z
			* get_new_board_after_movement

	* Ajout de Solver.py contenant 
		* main
		* usage 
		* open_file
		* resolve
		* simplify_list_of_mouvement

	* Ajout de fichiers contenant un objet Board, numérotés de 1 à 10.

	* solver.py s'ouvre via la console, avec en parametre un fichier.

	* L'ajout des methodes hash, permet de mettre les objets dans des dictionnaires.
