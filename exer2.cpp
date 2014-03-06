#include <iostream>
#include <string>
#include <vector>
#include <utility>  
#include <functional>
#include <assert.h>

using INTEGER_ARRAY = std::vector<int>;
using MATRIX = std::vector<INTEGER_ARRAY>;
using MATRIX_CREF = const MATRIX&;
using MATRIX_PROPERTY_FUNC = std::function<bool(MATRIX_CREF)>;
using MATRIX_PROPERTIES = std::vector< std::pair <MATRIX_PROPERTY_FUNC, std::string>>;
using MATRIX_PROPERTIES_CREF = const MATRIX_PROPERTIES&;

void assert_matrix(const MATRIX& matrix){
    const int rows = matrix.size();
    for(auto& row: matrix){
        assert(row.size() == rows);
    }
}

bool anwtrigwnikos(MATRIX_CREF matrix) {
    assert_matrix(matrix);
    for (int i = 1; i < matrix.size(); ++i){
        for (int j = 0; j < i; ++j){
            if (matrix [j] [i] != 0){
                 return false;
            }
        }
    }
    return true;
}

bool katwtrigwnikos(MATRIX_CREF matrix) {
    assert_matrix(matrix);
    for (int j = 1;j < matrix.size(); ++j){
        for (int i = 0;i < j; ++i){
            if (matrix [j] [i] != 0){
                return false;
            }
        }
    }
    return true;
}

bool symetrikos(MATRIX_CREF matrix) {
    assert_matrix(matrix);
    for (int i=0; i < matrix.size(); ++i){
        for (int j=0;j < matrix.size(); ++j){
            if ( matrix[i][j] != matrix[j][i]){
                return false;
            }
        }
    }
    return true;
}

bool araios(MATRIX_CREF matrix) {
    assert_matrix(matrix);
    int count=0;
    for (int i=0;i < matrix.size(); ++i){
        for (int j=0; j < matrix.size(); ++j){
              if (matrix[i][j] == 0){
                   count++;
            }
        }
    }
    return count >= matrix.size()*matrix.size()*80/100;
}

MATRIX read_matrix(int N) {
    int input;
    MATRIX matrix;
    for(int row = 0; row < N; ++row){
        INTEGER_ARRAY new_row;
        for(int col = 0; col < N; ++col){
            std::cout << row << ":" << col << " -> ";
            std::cin >> input;
            new_row.push_back(input);
        }
        matrix.push_back(new_row);
    }
    assert_matrix(matrix);
    return matrix;
}

void show_property(bool isTrue, const std::string& name) {
    std::cout << (isTrue ? "" : "δεν ")   << "ειναι " << name << std::endl;
}

void show_properties(MATRIX_CREF matrix, MATRIX_PROPERTIES_CREF properties) {
    std::cout << "Ιδιοτητες: " << std::endl;
    for(auto& property : properties){
        show_property(property.first(matrix), property.second);
    }
}

int main() {
    auto m = read_matrix(2);

    MATRIX_PROPERTIES properties = {
        std::make_pair (anwtrigwnikos, "ανω τριγωνικος"),
        std::make_pair (katwtrigwnikos,"κατω τριγωνικος"),
        std::make_pair (symetrikos,"συμμετρικος"),
        std::make_pair (araios,"αραιος"),
    };

    show_properties(m, properties);
}

