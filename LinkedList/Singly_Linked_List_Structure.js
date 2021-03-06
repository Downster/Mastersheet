// piece of data - val
//reference to next node - next

class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }
    push(val) {
        let newNode = new Node(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = this.head
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
        return this

    }

    pop() {
        if (!this.head) return undefined;
        let current = this.head
        let newTail = current
        while (current.next) {
            newTail = current;
            current = current.next;
        }
        this.tail = newTail;
        this.tail.next = null;
        this.length--;
        if (this.length === 0) {
            this.head = null;
            this.tail = null;
        }
        return current;
    }

    shift() {
        if (!this.head) return undefined;
        let current = this.head;
        this.head = current.next;
        this.length--;
        return current;
    }

    unshift(val) {
        let newHead = new Node(val)
        if (!this.head) {
            this.head = newHead;
            this.tail = this.head;
        } else {
            newHead.next = this.head;
            this.head = newHead;
            this.length++;
            return this;
        }
    }

    get(index) {
        if (index < 0 || index >= length) return null;
        let count = 0;
        let current = this.head;
        while (count !== index) {
            current = current.next;
        }
        return current;
    }

    set(val, index) {
        let foundNode = this.get(index)
        if (foundNode) {
            foundNode.val = val;
            return true;
        }
        return false;
    }

    insert(val, index){
        if (index < 0 || index > length) return false;
        if (index === length) return !!this.push(val);
        if (index === 0) return !!this.unshift(val);
        let newNode = new Node(val);
        let previousNode = this.get(index - 1)
        let nextNode = previousNode.next;
        previousNode.next = newNode;
        newNode.next = nextNode;
        this.length++;
        return true;
    }

    remove(index) {
        if (index < 0 || index > length) return undefined;
        if (index === length - 1) return this.pop();
        if (index === 0) return this.shift();
        let previousNode = this.get(index - 1);
        let removed = previousNode.next;
        previousNode.next = removed.next;
        this.length--;
        return removed;
    }

    reverse() {
        let node = this.head;
        this.head = this.tail;
        this.tail = node;
        let next;
        let prev = null;
        for (let i = 0; i < this.length; i++){
            next = node.next;
            node.next = prev;
            prev = node;
            node = next;
        }
        return this;

    }
}
