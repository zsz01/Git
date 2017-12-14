#include "stdafx.h"
#include <iostream>
#include <queue>
using namespace std;

unsigned cnt = 0;
unsigned bfscnt = 0;
unsigned Astarcnt = 0;

struct Point {
	int x;
	int y;
	Point(int xx = 0, int yy = 0) {
		x = xx;
		y = yy;
	}
	Point operator +(const Point &p) const{
		return Point(x + p.x, y + p.y);
	}
};
struct Mat {
	int m[4][4];
	unsigned cost = 0;
	Mat(int matrix[4][4]) {
		for (int i = 1; i <= 3; ++i) {
			for (int j = 1; j <= 3; ++j) {
				m[i][j] = matrix[i][j];
			}
		}
	}

	bool operator ==(const Mat &p)const {
		for (int i = 1; i <= 3; ++i) {
			for (int j = 1; j <= 3; ++j) {
				if (p.m[i][j] != m[i][j]) {
					return false;
				}
			}
		}
		return true;
	}
	friend bool operator <(const Mat &a, const Mat &b)
	{
		return a.cost > b.cost;
	}
};

int predictcost(const Mat a, const Mat b) {
	int cost = 0;
	for (int i = 1; i <= 3; ++i) {
		for (int j = 1; j <= 3; ++j) {
			bool flag = true;
			for (int k = 1; k <= 3 && flag; ++k) {
				for (int w = 1; w <= 3 && flag; ++w) {
					if (a.m[i][j] == b.m[k][w]) {
						cost += abs(i - k) + abs(j - w);
						flag = false;
					}
				}
			}
		}
	}
	return cost;
}

int temp[4][4];
void initial() {
	for (int i = 1; i <= 3; ++i) {
		for (int j = 1; j <= 3; ++j) {
			cin >> temp[i][j];
		}
	}
}
bool isOk(const Point p) {
	return p.x >= 1 && p.x <= 3 && p.y >= 1 && p.y <= 3;
}
Point findcur(const Mat t) {
	Point cur;
	bool flag = true;
	for (int i = 1; i <= 3 && flag; ++i) {
		for (int j = 1; j <= 3 && flag; ++j) {
			if (t.m[i][j] == 0) {
				cur.x = i;
				cur.y = j;
				flag = false;
			}
		}
	}
	return cur;
}


void bfs(Mat init, Mat dest) {
	queue<Mat> q;
	q.push(init);
	cnt = 0;
	bfscnt = 0;
	unsigned size = 1;
	while (!q.empty()) {
		Mat t = q.front();
		q.pop();
		bfscnt += 1;
		size -= 1;
		if (t == dest) {
			while (!q.empty()) {
				q.pop();
			}
			break;
		}
		else {
			Point cur = findcur(t);
			const Point Dir[4] = { Point(0,1),Point(0,-1),Point(1,0),Point(-1,0) };
			for (int i = 0; i < 4; ++i) {
				Point change = Dir[i] + cur;
				if (isOk(change)) {
					swap(t.m[change.x][change.y], t.m[cur.x][cur.y]);
					q.push(t);
					swap(t.m[change.x][change.y], t.m[cur.x][cur.y]);
				}
			}
			if (size == 0) {
				cnt += 1;
				size = q.size();
			}
		}
	}
}

void Astar(Mat init, Mat dest) {
	priority_queue<Mat> q;
	q.push(init);
	Astarcnt = 0;
	unsigned size = 1;
	while (!q.empty()) {
		Mat t = q.top();
		q.pop();
		Astarcnt += 1;
		if (t == dest) {
			while (!q.empty()) {
				q.pop();
			}
			break;
		}
		else {
			Point cur = findcur(t);
			const Point Dir[4] = { Point(0,1),Point(0,-1),Point(1,0),Point(-1,0) };
			for (int i = 0; i < 4; ++i) {
				Point change = Dir[i] + cur;
				if (isOk(change)) {
					unsigned temp_cost = t.cost;
					swap(t.m[change.x][change.y], t.m[cur.x][cur.y]);
					t.cost = predictcost(t, dest);
					q.push(t);
					swap(t.m[change.x][change.y], t.m[cur.x][cur.y]);
					t.cost = temp_cost;
				}
			}
		}
	}
}


int main() {
	printf("初始九宫格:\n");
	initial();
	Mat init(temp);
	printf("目的九宫格:\n");
	initial();
	Mat dest(temp);
	init.cost = predictcost(init, dest);

	bfs(init,dest);
	Astar(init, dest);

	printf("总过需要移动:%d次\n", cnt);
	printf("bfs计算%d个状态\n", bfscnt);
	printf("Astar计算%d个状态\n", Astarcnt);
	getchar();
	getchar();
	return 0;
}
