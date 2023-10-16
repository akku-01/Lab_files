#include <iostream>
#include <stack>
using namespace std;

// Define a structure to represent a node in the abstract syntax tree (AST)
struct TreeNode {
    string label; // Non-terminal or terminal symbol
    int value;    // Value associated with terminals (E in this case)
    TreeNode* left;
    TreeNode* right;

    TreeNode(string label) : label(label), value(0), left(nullptr), right(nullptr) {}
    TreeNode(string label, int value) : label(label), value(value), left(nullptr), right(nullptr) {}
};

// Define a stack to store the AST nodes
stack<TreeNode*> astStack;

// Function to create a new AST node
TreeNode* createNode(string label, int value = 0) {
    return new TreeNode(label, value);
}

// Semantic action for E -> integer
void EIntegerAction(TreeNode* node) {
    int value = node->value;
    astStack.push(node);
    cout << "E -> " << value << endl;
}

// Semantic action for E -> E1 + E2
void EAddAction(TreeNode* E1, TreeNode* E2) {
    TreeNode* node = createNode("E");
    node->left = E1;
    node->right = E2;
    astStack.push(node);
    cout << "E -> E + E" << endl;
}

// Semantic action for E -> E1 - E2
void ESubtractAction(TreeNode* E1, TreeNode* E2) {
    TreeNode* node = createNode("E");
    node->left = E1;
    node->right = E2;
    astStack.push(node);
    cout << "E -> E - E" << endl;
}

// Semantic action for if E then S1
void IfThenAction(TreeNode* E, TreeNode* S1) {
    TreeNode* node = createNode("if E then S1");
    node->left = E;
    node->right = S1;
    astStack.push(node);
    cout << "if E then S1" << endl;
}

// Semantic action for if E then S1 else S2
void IfThenElseAction(TreeNode* E, TreeNode* S1, TreeNode* S2) {
    TreeNode* node = createNode("if E then S1 else S2");
    node->left = E;
    node->right = S1;
    node->right->right = S2;
    astStack.push(node);
    cout << "if E then S1 else S2" << endl;
}

int main() {
    // Sample input: 2 + 3 - 1
    TreeNode* E = createNode("E");
    TreeNode* E1 = createNode("E", 2);
    TreeNode* E2 = createNode("E", 3);
    TreeNode* E3 = createNode("E", 1);

    EAddAction(E1, E2);
    ESubtractAction(E, E3);

    // Sample input: if (1) then {2} else {3}
    TreeNode* S1 = createNode("S1");
    TreeNode* S2 = createNode("S2");
    TreeNode* E4 = createNode("E", 1);

    IfThenAction(E4, S1);
    IfThenElseAction(E4, S1, S2);

    return 0;
}