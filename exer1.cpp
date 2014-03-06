#include <iostream>
#include <string>
#include <vector>

class Matrix{
        using INTEGER_ARRAY = std::vector<int>;
        using MATRIX = std::vector<INTEGER_ARRAY>;

        MATRIX _element;

        bool anwtrigwnikos() const {
            for (int i = 1;i < N;i++){
                for (int j = 0;j < i;j++){
                    if ( _element[j][i] != 0){
                         return false;
                    }
                }
            }
            return true;
        }

        int katwtrigwnikos() const {
            for (int j = 1;j < N;j++){
                for (int i = 0;i < j;i++){
                    if ( _element[j][i] != 0){
                        return false;
                    }
                }
            }
            return true;
        }

        int symetrikos() const {
            for (int i=0;i<N;i++){
                for (int j=0;j<N;j++){
                    if ( _element[i][j] != _element[j][i]){
                        return false;
                    }
                }
            }
            return true;
        }

        int araios() const
        {
            int count=0;
            for (int i=0;i < N; i++){
                for (int j=0;j<N ;j++){
                      if ( _element[i][j] == 0){
                           count++;
                    }
                }
            }
            return count >= N*N*80/100;
        }

        static void show_property(bool isTrue, const std::string& name) {
            std::cout << (isTrue ? "" : "δεν ")   << "ειναι " << name << std::endl;
        }

    public:

        int N; 

        void populate(int size) {
            N = size;
            int input;
            _element.clear();
            for(int row = 0; row < N; ++row){
                std::vector<int> new_row;
                for(int col = 0; col < N; ++col){
                    std::cout << row << ":" << col << " -> ";
                    std::cin >> input;
                    new_row.push_back(input);
                }
                _element.push_back(new_row);
            }
        }

        void show_properties() {
            std::cout << "Ιδιοτητες: " << std::endl;
            show_property(anwtrigwnikos(), "ανω τριγωνικος");
            show_property(katwtrigwnikos(), "κατω τριγωνικος");
            show_property(symetrikos(), "συμμετρικος");
            show_property(araios(), "αραιος");

        }
};




int main() {
     Matrix m;
     m.populate(2);
     m.show_properties();
}

