#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <tuple>
#include <limits>
#include <unordered_map>

using namespace std;

struct Edge {
    int to;
    int delay;
};

using Graph = vector<vector<Edge>>;
const int INF = numeric_limits<int>::max();

int shortestCommunicationDelay(int n, const vector<pair<int, int>>& nodes, int m, const vector<tuple<int, int, int, int>>& base_stations) {
    Graph graph(n + m + 1); // 节点编号从 1 到 n，基站编号从 n+1 到 n+m

    // 构建图：节点连接到基站，基站也连接到节点
    for (int i = 0; i < m; ++i) {
        int x, y, r, t;
        tie(x, y, r, t) = base_stations[i];
        int base_node = n + 1 + i; // 基站节点编号从 n+1 开始

        // 查找该基站覆盖范围内的节点
        for (int u = 1; u <= n; ++u) {
            int node_x = nodes[u - 1].first;
            int node_y = nodes[u - 1].second;
            if (abs(node_x - x) <= r && abs(node_y - y) <= r) {
                // 添加双向边：节点 <-> 基站
                graph[u].push_back({base_node, t});
                graph[base_node].push_back({u, 0});
            }
        }
    }

    // 使用 Dijkstra 算法查找最短路径
    vector<int> delay(n + m + 1, INF);
    delay[1] = 0; // 起始点为 1，延迟为 0
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({0, 1}); // (延迟, 节点)

    while (!pq.empty()) {
        auto [currentDelay, u] = pq.top();
        pq.pop();

        if (currentDelay > delay[u]) continue;

        // 遍历所有邻接节点
        for (const Edge& edge : graph[u]) {
            int v = edge.to;
            int t = edge.delay;

            // 如果通过当前节点的路径更短，更新延迟
            if (currentDelay + t < delay[v]) {
                delay[v] = currentDelay + t;
                pq.push({delay[v], v});
            }
        }
    }

    // 返回从节点 1 到节点 n 的最短延迟，如果不可达则返回 -1
    return delay[n] == INF ? -1 : delay[n];
}

int main() {
     //std::ios::sync_with_stdio(false);
    //std::cin.tie(nullptr);
    int n, m;
    cin >> n >> m;

    vector<pair<int, int>> nodes(n);
    for (int i = 0; i < n; ++i) {
        cin >> nodes[i].first >> nodes[i].second;
    }

    vector<tuple<int, int, int, int>> base_stations(m);
    for (int i = 0; i < m; ++i) {
        int x, y, r, t;
        cin >> x >> y >> r >> t;
        base_stations[i] = {x, y, r, t};
    }

    int result = shortestCommunicationDelay(n, nodes, m, base_stations);
    if (result == -1) {
        cout << "Nan" << endl;
    } else {
        cout << result << endl;
    }

    return 0;
}
