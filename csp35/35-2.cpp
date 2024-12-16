#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

// 读取输入数据
void read_input(string &s, int &n, vector<pair<char, char>> &mappings, int &m, vector<int> &queries) {
    string line;
    getline(cin, line);
    s = line.substr(1, line.size() - 2); // 去掉井号

    getline(cin, line);
    n = stoi(line);
    
    for (int i = 0; i < n; ++i) {
        getline(cin, line);
        mappings.emplace_back(line[1], line[2]);
    }

    getline(cin, line);
    m = stoi(line);

    getline(cin, line);
    istringstream iss(line);
    int k;
    while (iss >> k) {
        queries.push_back(k);
    }
}

// 计算字符经过 k 次变换的结果，使用周期优化
char transform_char(char ch, int k, const unordered_map<char, char> &f) {
    char current = ch;
    vector<char> cycle;
    unordered_map<char, int> position;
    
    // 找到环，并记录每个字符的位置
    while (position.find(current) == position.end()) {
        position[current] = cycle.size();
        cycle.push_back(current);
        current = f.at(current);
    }

    // 找到环的起始位置和长度
    int cycle_start = position[current];
    int cycle_length = cycle.size() - cycle_start;

    // 使用周期优化计算最终字符
    if (k >= cycle_start) {
        k = (k - cycle_start) % cycle_length + cycle_start;
    }
    return cycle[k];
}

// 解决问题
void solve() {
    // 读入数据
    
    string s;
    int n, m;
    vector<pair<char, char>> mappings;
    vector<int> queries;
    read_input(s, n, mappings, m, queries);

    // 构建字符替换表
    unordered_map<char, char> f;
    for (char c = 32; c < 127; ++c) {
        f[c] = c; // 初始化为自映射
    }
    for (const auto &mapping : mappings) {
        f[mapping.first] = mapping.second;
    }

    // 处理每个查询
    for (int k : queries) {
        string transformed = s;
        for (char &ch : transformed) {
            ch = transform_char(ch, k, f);
        }
        // 输出结果
        cout << "#" << transformed << "#" << endl;
    }
}

int main() {
    solve();
    return 0;
}
