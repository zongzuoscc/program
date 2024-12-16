#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <limits>

using namespace std;

// 补丁块的头部信息结构
struct BlockHeader {
    int startLine;
    int origLength;
    int newStartLine;
    int newLength;
};

// 补丁块的内容结构
struct Block {
    BlockHeader header;
    vector<string> origContent;
    vector<string> newContent;
};

// 解析补丁头部
bool parseBlockHeader(const string& line, BlockHeader& header) {
    regex pattern(R"(@@ -(\d+),(\d+) \+(\d+),(\d+) @@)");
    smatch matches;
    if (regex_match(line, matches, pattern)) {
        header.startLine = stoi(matches[1]);
        header.origLength = stoi(matches[2]);
        header.newStartLine = stoi(matches[3]);
        header.newLength = stoi(matches[4]);
        return true;
    }
    return false;
}

// 提取块内容
bool extractBlockContent(const vector<string>& lines, Block& block) {
    block.origContent.clear();
    block.newContent.clear();
    
    for (const string& line : lines) {
        if (line.empty()) continue;
        char firstChar = line[0];
        
        if (firstChar == ' ') {
            block.origContent.push_back(line.substr(1));
            block.newContent.push_back(line.substr(1));
        }
        else if (firstChar == '-') {
            block.origContent.push_back(line.substr(1));
        }
        else if (firstChar == '+') {
            block.newContent.push_back(line.substr(1));
        }
        else {
            return false;
        }
    }
    
    return block.origContent.size() == block.header.origLength &&
           block.newContent.size() == block.header.newLength;
}

// 在原文件中查找最佳匹配位置
pair<int, int> findBestMatch(const vector<string>& fileLines, 
                            const vector<string>& content,
                            int startLine, int length, int prevEnd) {
    int bestDelta = numeric_limits<int>::max();
    int bestPos = -1;
    
    for (int delta = -length + 1; delta < length; delta++) {
        int pos = startLine + delta - 1;
        if (pos < prevEnd || pos + length > fileLines.size()) {
            continue;
        }
        
        bool match = true;
        for (int i = 0; i < length; i++) {
            if (pos + i >= fileLines.size() || fileLines[pos + i] != content[i]) {
                match = false;
                break;
            }
        }
        
        if (match) {
            if (abs(delta) < abs(bestDelta) || 
                (abs(delta) == abs(bestDelta) && delta < bestDelta)) {
                bestDelta = delta;
                bestPos = pos;
            }
        }
    }
    
    return {bestPos, bestDelta};
}

// 应用补丁
string applyPatch(vector<string>& fileLines, vector<string>& patchLines) {
    // 移除注释行
    vector<string> cleanPatchLines;
    for (const string& line : patchLines) {
        if (!line.empty() && line[0] != '#') {
            cleanPatchLines.push_back(line);
        }
    }
    
    // 检查是否有有效的补丁块
    bool hasValidBlock = false;
    for (const string& line : cleanPatchLines) {
        if (line.substr(0, 3) == "@@ ") {
            hasValidBlock = true;
            break;
        }
    }
    if (!hasValidBlock) {
        return "Patch is damaged.";
    }
    
    // 分割补丁块
    vector<Block> blocks;
    vector<string> currentBlockLines;
    Block currentBlock;
    
    for (const string& line : cleanPatchLines) {
        if (line.substr(0, 3) == "@@ ") {
            if (!currentBlockLines.empty()) {
                if (!extractBlockContent(currentBlockLines, currentBlock)) {
                    return "Patch is damaged.";
                }
                blocks.push_back(currentBlock);
                currentBlockLines.clear();
            }
            if (!parseBlockHeader(line, currentBlock.header)) {
                return "Patch is damaged.";
            }
        }
        else {
            currentBlockLines.push_back(line);
        }
    }
    
    if (!currentBlockLines.empty()) {
        if (!extractBlockContent(currentBlockLines, currentBlock)) {
            return "Patch is damaged.";
        }
        blocks.push_back(currentBlock);
    }
    
    // 应用每个块
    int prevEnd = 0;
    int lineOffset = 0;
    
    for (size_t i = 0; i < blocks.size(); i++) {
        Block& block = blocks[i];
        block.header.startLine += lineOffset;
        
        // 找到最佳匹配位置
        auto [bestPos, delta] = findBestMatch(fileLines, block.origContent,
                                            block.header.startLine,
                                            block.header.origLength, prevEnd);
        
        if (bestPos == -1) {
            return "Patch is damaged.";
        }
        
        // 应用修改
        fileLines.erase(fileLines.begin() + bestPos,
                       fileLines.begin() + bestPos + block.header.origLength);
        fileLines.insert(fileLines.begin() + bestPos,
                        block.newContent.begin(), block.newContent.end());
        
        prevEnd = bestPos + block.header.origLength;
        lineOffset = delta;
    }
    
    // 构建结果字符串
    string result;
    for (size_t i = 0; i < fileLines.size(); i++) {
        result += fileLines[i];
        if (i < fileLines.size() - 1) {
            result += '\n';
        }
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    // 读取输入
    int n;
    cin >> n;
    cin.ignore(); // 忽略换行符
    
    vector<string> fileLines(n);
    for (int i = 0; i < n; i++) {
        getline(cin, fileLines[i]);
    }
    
    // 读取补丁
    vector<string> patchLines;
    string line;
    while (getline(cin, line)) {
        patchLines.push_back(line);
    }
    
    // 应用补丁并输出结果
    cout << applyPatch(fileLines, patchLines) << endl;
    
    return 0;
}
