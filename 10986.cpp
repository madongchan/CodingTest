#include <iostream>
#include <vector>
using namespace std;

int main()
{
	// 배열의 수, 나눌 값 선언 후 입력 받음
	int N, M;
	cin >> N >> M;
	// 수 N개 배열
	vector<long long> A(N + 1, 0);
	// 구간 합을 M으로 나눈 후의 배열
	vector<long long> S(N + 1, 0);

	// 정답 변수 초기화
	long long result = 0;

	// 구간 합을 구한다 수식은 S[i] = S[i - 1] + A[i]
	for (int i = 1; i <= N; i++)
	{
		long long input;
        cin >> input;
		S.at(i) = S.at(i - 1) + input;
	}
	// S.at(i)를 값을 M으로 나누기
	// count 벡터를 만들어 nCr에서 r은 두쌍이니까 2이고, n을 구하기 위해 vector를 통해 각 인덱스가 나머지 값이고 vector 인덱스 안의 값이 n을 의미하게 구성
	vector<long long> count(M, 0);
	count[0] = 1; // S[0]의 나머지 0을 미리 세어줍니다.
	for (int i = 1; i <= N; i++)
	{
		count.at(S.at(i) % M)++;
	}


	// count에서 인덱스마다  Conbination을 통해 2쌍을 뽑아 경우의 수를 result에 더하기
	// nCr 수식은 n! / ((n-r)! * r!)
	/*
	nC2 = n! / (2!(n-2)!)
	= (n × (n-1) × (n-2)!) / (2! × (n-2)!)
	= (n × (n-1)) / (2 × 1)
	= n(n-1)/2
	*/
	for (int i = 0; i < M; i++)
	{
		if (count.at(i) >= 2)
		{
			result += count.at(i) * (count.at(i) - 1) / 2;
		}
	}
	cout << result;
	return 0;
}