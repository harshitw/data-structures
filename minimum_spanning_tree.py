//spanning tree "" undirected and connected graph""

//prim's algorithm

#include<bits/stdc++.h>
using namespace std;

const int MAX = 1e4 + 5;
typedef pair<long long, int> p;
vector<bool> v[MAX];
vector<int> adj[MAX];

long long prim(int u){
    //min priority_queue based on first element of pair
    priority_queue<p, vector<p>, greater<p>> q;
    int t;
    long long cost;
    p p1;
    q.push(make_pair(0, u));
    while(!q.empty()){
        p1 = q.top();
        q.pop();
        u = p1.second;
        if(v[u]){
            continue;
        }
        cost += p1.first;
        v[u] = true;
        for(int i=0; i<adj[u].size(); i++){
            y = adj[u][i].second;
            if(!v[y]){
                q.push_back(adj[u][i]);
            }
        }
    }
    return cost;
}

int main(){
    int n, e;
    cin >> n >> e;
    long long weight, cost;
    int x, y;
    for(int i=0; i<n; i++){
        cin >> x >> y >> weight;
        adj[x].push_back(make_pair(y, weight));
        adj[y].push_back(make_pair(x, weight));
    }
    cost = prim(1);
    cout << cost;
    return 0;
}
