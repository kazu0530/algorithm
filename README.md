様々なアルゴリズムの実装例
データ構造や数論的アルゴリズムまで、様々な分野のアルゴリズムたちを C++17 で実装しています。
アルゴリズム系の研究開発において計算機実験が必要になる場面や、 プログラミングコンテストに参加する場面などを想定して、 「実装例」または「ライブラリ」として使用することを念頭に置いています。

　

分類	内容	具体例
MathNumberTheory	整数論的アルゴリズム	素因数分解、最大公約数など
MathCombinatorics	組合せ論的アルゴリズム	modint、Nim など
MathAlgebra	代数的アルゴリズム	行列計算など
DataStructure	データ構造	Union-Find、セグメント木など
DataStructureOnTree	木上のクエリに答えるためのデータ構造	Euler ツアー、HL 分解など
GraphTheory	グラフアルゴリズム	強連結成分分解、木の直径など
GraphNetworkFlow	ネットワークフローアルゴリズム	Ford-Fulkerson 法など
DP	定型的な動的計画法やその他の処理	いもす法、LIS、CHT など
Geometry	計算幾何	円の交点など
String	文字列アルゴリズム	ローリングハッシュ、Suffix Array など
Others	その他	xorshift、サイコロなど
　


MathNumberTheory
整数論的アルゴリズムたちです

約数, 倍数
約数列挙
最大公約数 (Euclid の互除法)
最小公倍数
拡張 Euclid の互除法
素数
素数判定
素因数分解
確率的素数判定 (Miller-Rabin 法)
確率的素因数分解 (Pollard のロー法)
Euler のトーティエント関数
原始根
N 以下の素数の個数 (O(N^2/3))
エラトステネスの篩
エラトステネスの篩
エラトステネスの区間篩
高速素因数分解, 約数列挙, メビウス関数 (エラトステネスの篩風)
線形篩
アトキンの篩
方程式
中国剰余定理
中国剰余定理 (Garner 法)
ペル方程式
離散対数
平方剰余 (Tonelli–Shanks 法)
有理数
有理数
Stern-Brocot 木
その他
多倍長整数
ガウス整数
平衡三進法展開
floor sum
　


MathCombinatorics
組合せ論的アルゴリズムたちです

mod, 二項係数
modint
実行時に法が決まる modint
累乗
逆元
二項係数 (オーソドックス, n<=10^7, r<=10^7, p<=10^9)
二項係数 (愚直計算, n<=10^9, r<=10^7, p<=10^9)
二項係数 (漸化式計算, n<=10^9, r<=10^9, p<=10^7)
二項係数 (任意 mod, n<=10^7, r<=10^7, m<=10^9)
mod の値が大きいとき
様々な数
重複組合せ
カタラン数
分割数
スターリング数
ベル数
ベルヌーイ数
ソート
クイックソート
マージソート
ヒープソート
コムソート
Radix ソート
挿入ソート
その他のソート達
マトロイド
マトロイド上の Greedy 法
マトロイド交差
その他
Nim
LIS and LDS
　


MathAlgebra
行列計算など代数的計算に関するアルゴリズムです

行列
行列 (基本演算)
行列累乗, ランク, 連立一次方程式 (実数)
行列累乗, ランク, 連立一次方程式 (mod. p)
行列累乗, ランク, 連立一次方程式 (binary)
Toeplitz 行列 (乗算, 連立方程式が O(n^2))
巡回行列 (乗算が O(n^2))
コンパニオン行列
三重対角行列 (連立方程式が O(n))
Black Box Linear Algebra
多項式, 方程式
二次方程式
多項式 (実数係数)
多項式 (mod. p 係数)
きたまさ法 (俗称)
きたまさ法 with FFT (俗称)
多項式補間
畳み込み計算
FFT (高速フーリエ変換)
NTT (高速剰余変換)
高速アダマール変換
高速ゼータ変換
高速メビウス変換
添字 GCD 畳み込み
Karatsuba 法
形式的冪級数
形式的冪級数
形式的冪級数 (実行時 mod)
最適化
二分探索法 (方程式の解を 1 つ求める)
三分探索法
黄金探索法
Newton 法
単体法
分枝限定法
　


DataStructure
各種データ構造の実装です

Union-Find
Union-Find (union by size)
Union-Find (union by rank)
重みつき Union-Find
重みつき Union-Find (F2 体)
部分永続 Union-Find
undo つき Union-Find
Quick Find
Dynamic Connectivity
セグメント木
セグメント木
セグメント木 (遅延評価)
Starry Sky 木 (俗称)
マージソート過程保存木
等差数列区間加算木
二次元セグメント木
Binary Indexed 木
BIT
BIT 上二分探索 (k 番目の要素を求める)
BIT (区間加算, 区間和取得に両対応)
二次元 BIT
二次元 BIT (領域加算, 領域和取得に両対応)
RMQ
RMQ (セグメント木)
RMQ (Sparse Table)
平方分割
Mo 法
平衡二分探索木
RBST
Treap 木
AVL 木
Splay 木
赤黒木
永続データ構造
永続配列
完全永続 Union-Find 木
永続セグメント木
永続赤黒木
ハッシュ
Zobrist hash
木に対する hash
ヒープ
Skew Heap (マージ可能)
Paring Heap (マージ可能)
Radix Heap
Fibonacci Heap
その他
Binary Trie
Disjoint Sparse Table
並列二分探索
Cartesian 木
Wavelet 木
　


DataStructureOnTree
ツリー上のクエリ処理のためのデータ構造たちの実装です

木全般
部分木サイズ, LCA など
LCA
LCA (ダブリング)
LCA (Euler Tour)
LCA (HL 分解)
テクニック
Euler Tour (頂点上)
Euler Tour (辺上のクエリ)
HL 分解
重心分解
Link-Cut 木
マージテク (俗称)
DSU on Tree
その他の問題
Level Ancester
　


GraphTheory
グラフ理論全般のアルゴリズムです

DFS・BFS
DFS (連結成分を数える)
BFS (重みなしグラフの最短路)
トポロジカルソート (DFS)
トポロジカルソート (BFS)
サイクル検出 (DFS)
サイクル検出 (BFS)
サイクル検出 (Union-Find)
二部グラフ判定 (DFS)
二部グラフ判定 (BFS)
二部グラフ判定 (Union-Find)
連結成分分解
強連結成分分解
橋, 関節点列挙 (Low-Link)
二重辺連結成分分解
二重頂点連結成分分解
2-SAT
ツリー
ツリーの直径
ツリーの重心
最短路
重みなしグラフの最短路 (BFS)
重みが 0, 1 のみのグラフの最短路 (0-1 BFS)
単一始点最短路 (Dijkstra 法, 正辺のみ)
単一始点最短路 (Bellman-Ford 法, 負辺対応)
全頂点対間最短路 (Floyd-Warshall 法)
全頂点対間最短路 (Johnson 法)
k-最短路
SPFA
その他
最小全域木 (Kruskal 法)
最小有向全域木 (Chu-Liu/Edmonds 法)
有向 Euler 路
無向 Euler 路
彩色数 (O(n2^n))
最大安定集合問題 (O(1.381^n))
最大クリーク列挙（O(1.443^n)）
最小シュタイナー木 (O(n 3^t + n^2 2^t + n^3))
　


GraphNetworkFlow
グラフネットワークフロー関連のアルゴリズムです

最大流
最大流 (Ford-Fulkerson 法)
最大流 (Dinic 法)
最小費用流
最小費用流 (Primal-Dual 法, 正辺のみ)
最小費用流 (Primal-Dual 法, 負辺対応)
最小費用最大流 (Primal-Dual 法, 正辺のみ)
最小費用最大流 (Primal-Dual 法, 負辺対応)
最小費用循環流 (Cost-Scaling, 負閉路OK)
カット
最小カット (= 最大流)
全域最小カット（Stoer-Wanger 法）
全頂点対間最小カット (Nagamochi-Ibaraki 法)
Gomory-Hu 木
マッチング
二部マッチング (Hopcroft-Karp 法)
重みつき二部マッチング (Hungarian 法)
一般グラフの最大マッチング (Edmonds 法)
一般グラフの最大マッチング (行列補間)
　


DP
定型的な動的計画法やその他の処理です

典型処理
累積和
二次元累積和
いもす法 (俗称)
二次元いもす法 (俗称)
スライド最小値
典型的 DP
転倒数
LIS
LCS
編集距離
重みつき区間スケジューリング問題
ヒストグラム長方形面積最大化
最適二分探索木
Set Cover
k-Cover (O(n 2^n))
k-partition (O(n^3 2^n))
DP パターン例
ナップサック DP
区間分割型ナップサック DP
bitDP
桁 DP
部分列 DP
ダブリング DP
木 DP
全方位木 DP (俗称)
二乗の木 DP (俗称)
DP 高速化テクニック
累積和
スライド最小値
インライン DP (俗称)
Convex Hull Trick (傾き単調, クエリも単調)
Convex Hull Trick (傾き単調)
Convex Hull Trick (単調でなくてよい)
Monotone Minima
Divide and Conquer
Monge
Alien DP
戻す DP (俗称)
　


Geometry
幾何ライブラリです

全部乗せ
基本要素 (点, 線分, 円)
点, 線分, 三角形などの位置関係
点と線分の位置関係 (ccw)
点と三角形の包含関係
射影, 交差判定, 距離
射影
線分と線分の交差判定
線分と線分との距離
直線や円の交点
直線と直線の交点
円と直線の交点
円と円の交点
円と線分の交点
多角形
多角形の面積
点と多角形の包含判定
凸性判定
凸包
凸多角形の切断
ボロノイ図 (単純ver, O(N^3))
凸多角形の直径
円と円の共通部分の面積
円と多角形との共通部分の面積
接線
接線
共通接線 (2 円)
三次元幾何
三次元幾何一式
その他
最近点対
最近円対
線分併合
線分アレンジメント
3 点を通る円
アポロニウスの円
最小包含円
双対変換
kd 木
　


String
文字列アルゴリズムです

構文解析
LL(1) 再帰降下パーサ
文字列検索
ローリングハッシュ
二次元ローリングハッシュ
単一パターン検索 (KMP 法)
単一パターン検索 (Boyer-Moore 法)
複数パターン検索 (Aho-Corasick 法)
文字列系アルゴリズム
Z 法
Manacher 法
文字列系データ構造
Trie 木
Suffix Array
Palindromic 木 (AOJ 2292)
その他
各 index 以降で各文字が最初に登場する index を求める関数
split 関数
二次元盤面に番兵追加
二次元盤面を 90 度回転
　


Others
その他のアルゴリズムです

グリッド
グリッドの 4 近傍, 8 近傍
ハニカムの 6 近傍
ビット演算テクニック
XorShift, ランダムシャッフル
next_combination
部分集合の部分集合
探索法
α-β 探索
焼き鈍し法
A*
IDA*
Baby-Step Giant-Step 法
平面走査法
その他
デバッグストリーム, chmin, chmax
pn + r (n は非負整数) で表せる整数のうち, x 以上となる最小の整数
タイマー
サイコロ
曜日
四面体 (AOJ 2060)
