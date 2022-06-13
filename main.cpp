#include <iostream>
#include <utility>

using namespace std;

class student;

int main()
{
    int x;
    cin >> x;

    student st;
    for (int i = 0; i > x; i++){
        st.get_data();
        st.display_data();
    }
        return 0;

}


class student{
public :
    static string st_name;
    static int reg_no;
    static int arrs[4];
    student(string st, int reg, const int mats[4]){
        student::st_name = std::move(st);
        student::reg_no = reg;
        student::arrs = std::copy(mats);

    };
    static void get_data(){
        string st;
        int reg;
        int mat[4];
        cin >> st;
        cin >> reg;
        for (int & i : mat) {
            cin >> i;
        }
        student(st,reg,mat);
        

    }
    static void display_data(){
        cout << st_name << "\n";
        cout << reg_no << "\n";
        for(int & j:arrs ){
            cout << j << "n";
        }
        
    }

};

class project:student{
    
};
class lab:student{};