#include <vector>

struct Node {
    int val;
    Node* next;
    Node(int v) : val(v), next(nullptr) {}
};

class LinkedList {
public:
    LinkedList() {
        head = nullptr;
        tail = nullptr;
    }

    int get(int index) {
        Node* current = head;
        for (int currentIndex = 0; currentIndex <= index && current != nullptr; currentIndex++)
        {            if (currentIndex == index)
            {
                return current->val;
            }
            current = current->next;
        }
        return -1;
    }

    void insertHead(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr)
        {
            head = newNode;
            tail = newNode;
        }
        else
        {
            newNode->next = head;
            head = newNode;
        }
        
    }
    
    void insertTail(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr)
        {
            head = newNode;
            tail = newNode;
        }
        else
        {
            tail->next = newNode;
            tail = newNode;
        }
    }

    bool remove(int index) {
        Node* removeLink = nullptr;
        if (head == nullptr)
        {
            return false;
        }
        else if(index == 0)
        {
            removeLink = head;
            head = head->next;
            if (head == nullptr) tail = nullptr;
            delete removeLink;
            return true;
        }
        Node* previous = head;
        Node* current = head->next;
        for(int currentIndex = 1; currentIndex <= index && current != nullptr; currentIndex++)
        {
            if(currentIndex == index)
            {
                if(current == tail)
                {
                    tail = previous;
                    previous->next = nullptr;
                }else
                {
                    previous->next = current->next;
                }
                delete current;
                return true;
            }
            previous = current;
            current = current->next;
        }
        return false;
    }

    std::vector<int> getValues() {
        std::vector<int> vals;
        Node* current = head;
        while(current != nullptr)
        {
            vals.push_back(current->val);
            current = current->next;
        }
        return vals;
    }
    
    private:
        Node* head;
        Node* tail;
};