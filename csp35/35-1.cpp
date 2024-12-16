#include <iostream>
#include <string>
#include <map>
using namespace std;

// 判断密码的安全级别
int checkPasswordSecurity(const string &password) {
    int length = password.size();
    bool hasLetter = false;  // 是否包含字母
    bool hasDigit = false;   // 是否包含数字
    bool hasSpecial = false; // 是否包含特殊字符（* 或 #）
    map<char, int> charCount; // 记录字符出现的次数

    // 遍历密码，统计信息
    for (int i = 0; i < length; i++) {
        char c = password[i];
        // 判断字符类型
        if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) {
            hasLetter = true;
        } else if (c >= '0' && c <= '9') {
            hasDigit = true;
        } else if (c == '*' || c == '#') {
            hasSpecial = true;
        }
        // 统计字符出现次数
        charCount[c]++;
    }

    // 高安全级别判断
    bool highSecurity = true;
    for (auto it : charCount) {
        if (it.second > 2) {
            highSecurity = false; // 如果某字符出现超过2次，不满足高安全级别
            break;
        }
    }
    if (length >= 6 && hasLetter && hasDigit && hasSpecial && highSecurity) {
        return 2; // 高安全级别
    }

    // 中安全级别判断
    if (length >= 6 && hasLetter && hasDigit && hasSpecial) {
        return 1; // 中安全级别
    }

    // 如果不满足高和中安全级别，则为低安全级别
    return 0;
}

int main() {
    int n;
    cin >> n; // 输入密码个数
    cin.ignore(); // 忽略换行符

    for (int i = 0; i < n; i++) {
        string password;
        getline(cin, password); // 输入每个密码
        cout << checkPasswordSecurity(password) << endl; // 输出安全级别
    }

    return 0;
}
