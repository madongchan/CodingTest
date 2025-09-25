#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int N, M;
	cin >> N >> M;

	// 원본 배열을 저장할 벡터 A를 생성하고 초기화한다. 0번 인덱스를 패딩으로 사용하기 위해 N+1 크기로 만든다.
	vector<vector<int>> A(N + 1, vector<int>(N + 1, 0));

	// 벡터로 이중 배열 생성. 
	vector<vector<int>> S(N + 1, vector<int>(N + 1, 0));

	// 누적 합 2차원 벡터 S을 입력 값을 통해 채운다
	for(int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			// (i, j) 위치에 해당하는 값을 입력받습니다.
			cin >> A.at(i).at(j);
			// 누적 합을 계산한다.
			S.at(i).at(j) = 
			S.at(i - 1).at(j) + S.at(i).at(j - 1) - S.at(i - 1).at(j - 1) + A.at(i).at(j);
		}
	}

	// 누적 합 S를 채웠으니 M개의 쿼리를 돌면서 질의 문 처리
	for(int i = 1; i <= M; i++)
	{
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;

		int result = S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 - 1];
		cout << result << "\n";
	}
}