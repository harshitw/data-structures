#include<bits/stdc++.h>
using namespace std;

void edge(vector<int> adj[], int a, int b){
    adj[a].push_back(b);
    adj[b].push_back(a);
}

void dfsutil(int u, vector<int>adj[], vector<bool> &v){
    v[u] = true;
    cout << u << " ";
    for(int i=0; i<adj[u].size(); i++){
        if(!v[adj[u][i]]){
            dfsutil(adj[u][i], adj, v);
        }
    }
}

void dfs(vector<int> adj[], int n){
    vector<bool> v(n, false);
    for(int i=0; i<n; i++){
        if(!v[i]){
            dfsutil(i, adj, v);
        }
    }
}

int main(){
    int n, e;
    cin >> n >> e;
    vector<int> adj[n];
    int a, b;
    for(int i=0; i<e; i++){
        cin >> a >> b;
        edge(adj, a, b);
    }
    dfs(adj, n);
    return 0;
}
