#include <string>


class Dictionary {      
    private:             
        Dictionary_Element* head_element;
    public:
        void addElement(char new_element) {
            Dictionary_Element* temp = head_element;
            if (temp == nullptr) {
                head_element = new_element;
            } else {
                while (temp->next != nullptr) {
                    temp = temp->next;
                }
                Dictionary_Element* element;
                element->key = new_element;
                element->value = 1;
                temp->next = element;

            }
        }   

        void addAppearance(char element) {
            Dictionary_Element* temp = head_element;
            while (temp->next != nullptr) {
                if (temp->key == element) {
                    temp->value++;
                }
            }
        }

        int getAmount(char element) {
            Dictionary_Element* temp = head_element;
            while (temp->next != nullptr) {
                if (temp->key == element) {
                    return temp->value;
                }
            }
            return 0;
        }
};

class Dictionary_Element {
    public: 
        char key;
        int value;
        Dictionary_Element* next;
};


// Retorna una lista que tiene la cantidad de apariciones de cada character
Dictionary getFrequencies(std::string word) {
    Dictionary frequencies_dict;

    for (std::string::size_type i = 0; i < word.size(); i++) {
        char curr_char = word[i];
		if (frequencies_dict.getAmount(curr_char) == 0) {
            frequencies_dict.addElement(curr_char);
        } else {
            frequencies_dict.addAppearance(curr_char);
        }
	}
}

// Falta hacer una lista que se le agregue cada elemento en orden.
// Es decir, cada vez que va aingresar un elemento solo verifica que sea mayor o menor
// Es como agregar en una posicion en una lista enlazada. Pero en vez de buscar la posicion que da el usuario
// lo que hace es buscar que esté entre dos números, el de la izquierda es menor y el next es mayor

// cree una clase Node
// Para que pueda tener un head nada más que es donde epieza la lista

// Luego es crear el arbol, pero primero haga eso manana le ayudo con la otra vara


