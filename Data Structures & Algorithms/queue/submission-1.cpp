struct Node {
        Node* next;
        Node* previous;
        int val;
        Node(int val): next(nullptr), previous(nullptr), val(val) {}
};

class Deque {
public:
    Deque() {
        size = 0;
    }

    bool isEmpty() {
        return size == 0;
    }

    void append(int value) {
        Node* newNode = new Node(value);
        if (size == 0) {
            left = newNode;
            right = newNode;
        } else {
            newNode->previous = right;
            right->next = newNode;
            right = newNode;
        }
        size++;
    }

    void appendleft(int value) {
        Node* newNode = new Node(value);
        if (size == 0) {
            left = newNode;
            right = newNode;
        } else {
            newNode->next = left;
            left->previous = newNode;
            left = newNode;
        }
        size++;
    }

    int pop() {
        if (size == 0) {
            return -1;
        } else {
            int val = right->val;
            Node* deletionCandidate = right;
            if (size > 1) {
                right = right->previous;
                right->next = nullptr;
            } else {
                left = nullptr;
                right = nullptr;
            }
            delete deletionCandidate;
            size--;
            return val;
        }
    }

    int popleft() {
        if (size == 0)
        {
            return -1;
        } else {
            int val = left->val;
            Node* deletionCandidate = left;
            if (size > 1) {
                left = left->next;
                left->previous = nullptr;
            } else {
                left = nullptr;
                right = nullptr;
            }
            delete deletionCandidate;
            size--;
            return val;
        }
    }
private:
    int size;
    Node* left;
    Node* right;
};