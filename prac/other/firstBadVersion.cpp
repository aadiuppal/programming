#include<iostream>
using namespace std;

bool isBadVersion(int a){
  if(a >= 1702766719){
    return true;
  }
  return false;
}

int firstBadVersion(int n) {
    int i = 1;
    int j = n;
    int v = n;
    int m;
    int count = 0;
    while(i<=j){
        //cout<<i<<" "<<j<<"$$";
        if (i==j){
          if (isBadVersion(i)){
            v = min(v,i);
          }
         break;
        }
        m = (i/2+j/2);
        count++;
        if (isBadVersion(m)){
            v = m;
            j = m-1;
        }else{
            i = m+1;
        }
    }
    cout<<"count"<<count<<"\n";
    return v;
}


int main(){
  cout<<firstBadVersion(2126753390)<<"\n";
  return 0;
}
