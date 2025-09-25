#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	// 입력으로 배열의 크기와 문제 풀이 갯 수를 받는다
	int N, M;
	cin >> N >> M;
	// 합 배열을 초기화
	int S[100001] = {0};
	// 합 배열을 계산한다
	for (int i = 1; i <= N; i++)
	{
		int temp;
		cin >> temp;
		// 합 배열에 현재 값을 누적한다
		S[i] = S[i - 1] + temp;
	}
	// 합 배열 만들었으니 문제 풀이 갯 수 만큼 반복
	for (int i = 0; i < M; i++)
	{
		int start, end;
		cin >> start >> end;
		// 시작 구간과 종료 구간의 구간 합을 구하고 출력한다
		cout << S[end] - S[start - 1] << "\n";
	}
}