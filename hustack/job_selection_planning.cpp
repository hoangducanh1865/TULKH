#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define ll long long
#define ld long double

#define pii pair<int, int>
#define pll pair<ll, ll>
#define pf pair<float, float>
#define pd pair<double, double>
#define pld pair<ld, ld>

#define vc vector<char>
#define vvc vector<vc>
#define vs vector<string>
#define vvs vector<vs>
#define vi vector<int>
#define vvi vector<vi>
#define vll vector<ll>
#define vvll vector<vll>
#define vf vector<float>
#define vvf vector<vf>
#define vd vector<double>
#define vvd vector<vd>
#define vld vector<ld>
#define vvld vector<vld>

#define vpii vector<pii>
#define vvpii vector<vpii>
#define vpll vector<pll>
#define vvpll vector<vpll>
#define vpf vector<pf>
#define vvpf vector<vpf>
#define vpd vector<pd>
#define vvpd vector<vpd>
#define vpld vector<pld>
#define vvpld vector<vpld>

#define all(a) a.begin(), a.end() // Used for 0-based indexing
#define range(a, l, r) a.begin() + l, a.begin() + r + 1
#define sz(a) (int)(a).size()
#define len(a) (int)(a).length()

#define gcd(a, b) __gcd(a, b)
#define lcm(a, b) (a * b / gcd(a, b))

#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define FOD(i, a, b) for (int i = a; i >= b; i--)

#define pb push_back
#define is insert
#define er erase
#define rs resize
#define el cout << endl
#define dbg(x) cout << "# " << #x << " = " << x << endl
#define sdbg cout << "S"; FOR(i,1,36) {cout << "#";} el;
#define edbg cout << "E"; FOR(i,1,36) {cout << "#";} el;
#define char_to_int_lower_case(x) (int)(x - 'a' + 1)
#define char_to_int_upper_case(x) (int)(x - 'A' + 1)
#define int_to_char_lower_case(x) (char)('a' + x - 1)
#define int_to_char_upper_case(x) (char)('A' + x + 1)
#define sort_in(a, l, r) sort(range(a, l, r), [](const auto &x, const auto &y) {return x < y});
#define sort_de(a, l, r) sort(range(a, l, r), [](const auto &x, const auto &y) {return x > y});
#define sort_pa(a, l, r) sort(range(a, l, r), [](const auto &x, const auto &y) {if (x.fi != y.fi) return x.fi < y.fi; else return x.se < y.se; })
#define bin_search_low(a, l, r, x) lower_bound(range(a, l, r), x)
#define bin_search_up(a, l, r, x) upper_bound(range(a, l, r), x)
#define merge_fake(a, b, c) a.rs(sz(b) + sz(c)); merge(all(b), all(c), a.begin()) // Used for 0-based indexing

#define MOD = 1000000007;
#define INF INT_MAX
#define LLINF LLONG_MAX
const float FINF = 1e30f; // FLT_MAX
const double DINF = 1e18; // DBL_MAX
const long double LDINF = 1e18L; // LDBL_MAX

#define fastio ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

int main() {
    fastio;
    // freopen("inputs/input_.in", "r", stdin);

    int n;
    cin >> n;

    vpii jobs;
    FOR(i, 1, n) {
        int d, p;
        cin >> d >> p;
        jobs.pb({d, p});
    }

    sort(jobs.begin(), jobs.end(), [] (const auto &x, const auto &y) {return x.fi < y.fi;});

    priority_queue<int, vector<int>, greater<int>> pq;
    for(auto [d, p] : jobs) {
        pq.push(p);
        if((int)pq.size() > d) pq.pop();
    }

    ll ans = 0;
    while(!pq.empty()) {
        ans += pq.top();
        pq.pop();
    }

    cout << ans;

    return 0;
}
