#include <iostream>
#include <vector>
#include <set>
using namespace std;

// Função para trocar dois elementos
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

// Função para gerar permutações
void permutacoes(vector<int> &nums, int start, set<vector<int>> &result) {
    if (start == nums.size() - 1) {
        result.insert(nums); // Armazena a permutação no conjunto
    } else {
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]); // Troca
            permutacoes(nums, start + 1, result); // Chamada recursiva
            swap(nums[start], nums[i]); // Retorna ao estado original (backtrack)
        }
    }
}

// Função principal
int main() {
    vector<int> nums(4);
    cout << "Digite 4 numeros (podem ser repetidos): ";
    for (int i = 0; i < 4; i++) {
        cin >> nums[i];
    }

    set<vector<int>> result; // Conjunto para armazenar permutações únicas
    permutacoes(nums, 0, result);

    cout << "Permutacoes possiveis:" << endl;
    for (const auto &perm : result) {
        for (int num : perm) {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}
