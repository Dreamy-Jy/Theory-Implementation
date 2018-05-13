#include <iostream>

using namespace std;

struct Node
{
    int value;
    Node *left;
    Node *right;

    Node(int val) {
        this->value = val;
    }

    Node(int val, Node *left, Node *right) {
        this->value = val;
        this->left = left;
        this->right = right;
    }
};

bool DFS_PreOrder_find_recursive(const int &find, const Node *entry);
void DFS_PreOrder_traversal_iterative_recursive(const Node *entry);

Node *generateBinaryTree(){
    Node *root = new Node(2);

    root->right = new Node(5, nullptr, new Node(9, new Node(4), nullptr));
    root->left = new Node(7, new Node(2), new Node(6, new Node(5), new Node(11)));

    return root;
}

int main() {
    Node *root = generateBinaryTree();

    cout << (DFS_PreOrder_find_recursive(12, root) ? "I'm in the tree" : "I'm not in the tree") << endl;

    DFS_PreOrder_traversal_iterative_recursive(root);
}

bool DFS_PreOrder_find_recursive(const int &find, const Node *entry) {
    if (entry == nullptr)
        return false;

    if (entry->value == find)
        return true;

    return (DFS_PreOrder_find_recursive(find, entry->left) || DFS_PreOrder_find_recursive(find, entry->right));
}

void DFS_PreOrder_traversal_iterative_recursive(const Node *entry) {
    if (entry == nullptr)
        return;

    cout << entry->value << " ";

    DFS_PreOrder_traversal_iterative_recursive(entry->left);

    DFS_PreOrder_traversal_iterative_recursive(entry->right);
