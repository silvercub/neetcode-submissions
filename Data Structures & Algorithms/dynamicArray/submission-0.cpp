class DynamicArray {
public:

    DynamicArray(int capacity): capacity(capacity) {
        backingStorage = new int[capacity];
        size = 0;
    }

    int get(int i) {
        return backingStorage[i];
    }

    void set(int i, int n) {
        backingStorage[i] = n;
    }

    void pushback(int n) {
        if (size == capacity)
        {
            resize();
        }
        backingStorage[size] = n;
        size++;
    }

    int popback() {
        return backingStorage[--size];
    }

    void resize() {
        capacity *= 2;
        int* newStorage = new int[capacity];
        for (int index = 0; index < size; index++)
        {
            newStorage[index] = backingStorage[index];
        }
        delete[] backingStorage;
        backingStorage = newStorage;
        newStorage = NULL;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
private:
    int* backingStorage;
    int capacity;
    int size;
};
