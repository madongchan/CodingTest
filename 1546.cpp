#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    double result = 0; // 결과
    int M; // 점수 중 최대값
    int N; // 과목 갯 수
    cin >> N;
    vector<int> scores; // 점수들
    int value = 0;
    for (size_t i = 0; i < N; i++)
    {
        cin >> value;
        scores.push_back(value);
    }
    auto highestScore = max_element(scores.begin(), scores.end());
    if (highestScore != scores.end())
    {
        // 최대값이 있을 때
        for (size_t i = 0; i < N; i++)
        {
            result += static_cast<double>(scores.at(i)) / *highestScore * 100;
        }
        cout << result / N << endl;
    }
}
