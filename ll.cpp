#include<iostream>
#include<vector>
#include <algorithm>
#include  <initializer_list>


template<typename T>
class List final {
    public:
        class Node final {
            friend class List<T>;
            Node* _next;
            T _value;

            ~Node() {
                // std::cout << "deleting node: " << _value << std::endl;
                // you can write a unit test to prevent leaks!!!
            }

            Node(const T& value) : _value(value) {}

            Node* tail() { return _next == NULL ? this : _next->tail(); }

            void delete_subsequent_elements() {
                if(NULL != _next){
                    _next -> delete_subsequent_elements();
                    delete _next;
                    _next = NULL;
                }
            }

            public:
                const T& get_value() const { return _value; }
        };

        Node* get_tail() { return _head == NULL ? NULL : _head -> tail(); }

    private:
        Node* _head;

    public:
        class Iterator final {
            Node* _node;
            public:
                Iterator(Node* node) : _node(node) {}       

                Node* get_node() { return _node;}

                Node* operator->() { return _node;}

                Iterator& operator++() {
                    if(_node != NULL) {
                        _node = _node->_next;
                    }
                    return *this;
                }

                bool operator==(const Iterator& other) {
                    return _node == other._node;
                }


                bool operator!=(const Iterator& other) {
                    return _node != other._node;
                }
        };


        List(): _head(NULL) {}

        List(std::initializer_list<T> init_list) : _head(NULL) {
            std::cout << "here...." << std::endl;
            for(auto t: init_list){
                add(t);
            }
        }

        ~List() {
            if(NULL != _head){
                _head->delete_subsequent_elements();
                delete _head;
                _head = NULL;
            }
         }

        Iterator begin() { 
            return Iterator(_head); 
        }

        Iterator end() { 
            return Iterator(NULL); 
        }

        void shrink(int elements_to_drop){
            std::vector<Node*> to_delete;
            Node* new_head = NULL;
            int count = 0;
            // αυτο μπορεις να το κανεις καλυτερα... still an implementation detail!!
            for(Iterator iter = begin(); iter != end();  ++iter, ++count)
            {
                if(count < elements_to_drop){
                    to_delete.push_back(iter.get_node());
                }
                else {
                    new_head = iter.get_node();
                    break;
                }
            }
            _head = new_head;
            for_each( to_delete.begin(), to_delete.end(), [] (Node* node) { delete node; } );
        }
        
        void add(const T& t) {
            if(_head == NULL) {
                _head = new Node(t);
            } 
            else {
                get_tail()->_next = new Node(t);
            }
        }
       
};


int main(){
    auto mylist = List<int> { 1,2,3,4,5};

    for(List<int>::Iterator iter = mylist.begin(); iter != mylist.end();  ++iter){
        std::cout << iter->get_value() << std::endl;
    }

    mylist.shrink(3);
    std::cout << "After the shrink!" << std::endl;    

    for(List<int>::Iterator iter = mylist.begin(); iter != mylist.end();  ++iter){
        std::cout << iter->get_value() << std::endl;
    }
}
