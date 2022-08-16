#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int N;
    cin >> N;

    int arr[N];
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }
    int head;
    cin >> head;
    int size;
    cin >> size;
    int direction;
    cin >> direction;

    // dividing array into elements greater than head and smaller than head
    vector<int> greater;
    vector<int> smaller;
    smaller.push_back(0);
    smaller.push_back(size - 1);
    for (int i = 0; i < N; i++)
    {
        if (arr[i] > head)
            greater.push_back(arr[i]);
        else
            smaller.push_back(arr[i]);
    }
    int curr, distance;
    int total = 0;
    sort(smaller.begin(), smaller.end());
    sort(greater.begin(), greater.end());

    if(distance==0)
    {
        for(int i=smaller.size()-1; i>=0; i--){
            distance = abs(head - smaller[i]);
            total += distance;
            head = smaller[i];
        }
        total+=size-1;
        for(int i=0; i<greater.size(); i++){
            distance = abs(head - greater[i]);
            total += distance;
            head = greater[i];
        }
    }
    if(distance==1){
for(int i=0; i<greater.size(); i++){
            distance = abs(head - greater[i]);
            total += distance;
            head = greater[i];
        }
        total+=size-1;
        for(int i=smaller.size()-1; i>=0; i--){
            distance = abs(head - smaller[i]);
            total += distance;
            head = smaller[i];
        }
    }

    cout << total;

    return 0;
}